import logging

from project import BaseRepoProject

log = logging.getLogger(__name__)

class RepoWorkspaceUpdaterMirror(BaseRepoProject):

    name = 'repo_workspace_updater_mirror'

    repo_mirror_path = '~/repo/repo_workspace_updater.git'

    def on_repo_updated(self, git_repo):
        git_repo.remotes.origin.push()
        git_repo.remotes.upstream.push()
