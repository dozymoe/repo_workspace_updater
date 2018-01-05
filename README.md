Description
===========

Update workspace when a git repository's branch were updated.

This project is meant to be a cron task, or can be run manually.

Purpose of project, provides a central place to manage read-only workspaces that
was git cloned from repositories, as opposed to using git hooks.
When the repository were updated we expect the the workspace to also be updated,
usually used in automated servers.

Sample crontab entry:

    */15  *  *  *  * /home/USER/Workspace/repo_workspace_updater/run example

By default, project's `repo_branch` is set to `None`, meaning any new commit
will trigger update hooks, set new project `repo_branch` to `'master'` if you
want to monitor only the master branch.
