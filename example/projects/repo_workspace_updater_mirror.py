from lib.core import RepoProjectBase

class RepoWorkspaceUpdaterMirror(RepoProjectBase):

    repo_mirror_path = '/mnt/work/repo_workspace_updater'

    def on_repo_updated(self, git_repo):
        git_repo.remotes.origin.push()
