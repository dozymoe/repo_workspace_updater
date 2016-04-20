class BaseRepoProject(object):

    repo_mirror_path = None
    repo_branch = 'master'

    #current_commit = None
    #previous_commit = None

    project_path = None


    def __init__(self):
        self.current_commit = None
        self.previous_commit = None


    def onRepoUpdated(self, git_repo):
        raise NotImplemented()
