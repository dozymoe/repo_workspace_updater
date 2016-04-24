Description
===========

Update workspace when a git repository's branch were updated.

This project is meant to be a cron task, or can be run manually.

Purpose of project, provides a central place to manage read-only workspaces that
was git cloned from repositories, as opposed to using git hooks.
When the repository were updated we expect the the workspace to also be updated,
usually used in automated servers.

Sample cron script:

    #!/bin/bash

    cd ~/Workspace/repo_workspace_updater
    source .virtualenv/bin/activate
    cd src
    python main.py

You need to create `projects` directory (which could be a git repository) next
to `src/projects.example`.
