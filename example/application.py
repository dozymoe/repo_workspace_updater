from lib.core import ApplicationBase

from .projects.repo_workspace_updater_mirror import RepoWorkspaceUpdaterMirror

class Application(ApplicationBase):

    PROJECTS = [
        RepoWorkspaceUpdaterMirror,
    ]
