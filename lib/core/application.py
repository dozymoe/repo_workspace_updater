import dbm.gnu
from git import BadName, Repo
import logging
import os

from . import configuration

class ApplicationBase(object):

    PROJECTS = []

    config = None
    datastore = None
    logger = None
    repos = None

    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.repos = {}

        self.config = {}
        configuration.load_files_from_shell(self.config,
                configuration.generic_adapter)

        self.config['work_dir'] = os.path.dirname(os.path.realpath(__file__))

        root_dir = os.environ['ROOT_DIR']
        self.datastore = dbm.gnu.open(os.path.join(root_dir, self.config.get(
                'application.datastore', 'datastore.db')), 'cf')


    def check_repos(self):
        datastore_modified = False

        for repo_path, projects in self.repos.items():
            git = Repo(repo_path)
            for remote in git.remotes:
                remote.fetch()

            for project in projects:
                try:
                    if project.repo_branch:
                        branch = git.heads[project.repo_branch]
                        if git.head.commit != branch.commit:
                            branch.checkout()
                        if git.head.commit != branch.tracking_branch().commit:
                            git.remote().pull()

                    commit = git.head.commit
                except BadName:
                    continue

                triggered = False

                if project.current_commit != commit.hexsha:
                    triggered = True
                    self.logger.debug('%s: "%s" - "%s"', repo_path,
                            project.current_commit, commit.hexsha)

                elif project.custom_trigger():
                    triggered = True

                if triggered:
                    try:
                        project.on_repo_updated(git)
                        project.set_current_commit(commit.hexsha)
                        datastore_modified = True
                    except Exception as e:
                        self.logger.error(str(e))

        if datastore_modified:
            self.datastore.sync()


    def execute(self):
        for project_class in self.PROJECTS:
            project_obj = project_class(self)

            mirror_path = os.path.expanduser(project_obj.repo_mirror_path)
            if not mirror_path in self.repos:
                self.repos[mirror_path] = []
            self.repos[mirror_path].append(project_obj)

        self.check_repos()
