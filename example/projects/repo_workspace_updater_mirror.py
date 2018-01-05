from lib.core import RepoProjectBase

class RepoWorkspaceUpdaterMirror(RepoProjectBase):

    repo_mirror_path = '~/repo/repo_workspace_updater.git'

    def on_repo_updated(self, git_repo):
        git_repo.remotes.origin.push()
        git_repo.remotes.upstream.push()
