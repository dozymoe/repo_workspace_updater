#!/usr/bin/env python

import dbm.gnu
import logging
import os
import sys

from git import BadName, Repo

from projects import PROJECT_CLASSES

repos = {}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
log = logging.getLogger(__name__)


def check_repo():
    datastore_modified = False

    for repo_path in repos:
        git = Repo(repo_path)
        for project in repos[repo_path]:
            try:
                if project.repo_branch:
                    commit = git.commit(project.repo_branch)
                else:
                    commit = next(git.iter_commits())
            except BadName:
                continue

            if project.current_commit != commit.hexsha:
                log.debug('%s: "%s" - "%s"', repo_path, project.current_commit,
                        commit.hexsha)

                try:
                    project.on_repo_updated(git)
                    project.set_current_commit(commit.hexsha)
                    datastore_modified = True
                except Exception as e:
                    log.error(str(e))

    if datastore_modified:
        datastore.sync()


with dbm.gnu.open(os.path.join(BASE_DIR, 'datastore.db'), 'cf') as datastore:
    for project_class in PROJECT_CLASSES:
        project_obj = project_class(datastore)

        mirror_path = os.path.expanduser(project_obj.repo_mirror_path)
        if not mirror_path in repos:
            repos[mirror_path] = []
        repos[mirror_path].append(project_obj)

    check_repo()
