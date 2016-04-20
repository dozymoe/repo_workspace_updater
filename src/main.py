#!/usr/bin/env python

import os
import signal

from git import Repo

from projects import PROJECTS

repos = {}
running = True
interval = 60 # seconds

def signal_handler(signum, frame):
    log.info('CLOSING!!!!!!')
    global running
    running = False


def check_repo():
    for repo_path in repos:
        git = Repo(repo_path)
        for project in repos[repo_path]:
            commit = git.commit(project.repo_branch or 'master')

            if project.current_commit != commit.hexsha:
                project.previous_commit = project.current_commit
                project.current_commit = commit.hexsha
                project.onRepoUpdated(git)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

for project in PROJECTS:
    mirror_path = os.path.expanduser(project.repo_mirror_path)
    if not mirror_path in repos:
        repos[mirror_path] = []
    repos[mirror_path].append(project)

trigger = 0
while running:
    if trigger == 0:
        check_repo()
        trigger = interval
    else:
        trigger -= 1
    sleep(1)