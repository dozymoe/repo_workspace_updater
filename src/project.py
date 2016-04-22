class BaseRepoProject(object):

    name = 'base_repo_class'

    repo_mirror_path = None
    repo_branch = 'master'
    project_path = None

    datastore = None
    current_commit = None
    previous_commit = None


    def __init__(self, datastore):
        self.datastore = datastore

        self.current_commit = self._get_from_datastore('current_commit')
        self.previous_commit = self._get_from_datastore('previous_commit')


    def _get_from_datastore(self, field_name):
        try:
            datastr = self.datastore[self.name + '_' + field_name]
            if hasattr(datastr, 'decode'):
                return datastr.decode()
            else:
                return datastr
        except KeyError:
            return ''


    def _set_to_datastore(self, field_name, value):
        self.datastore[self.name + '_' + field_name] = value


    def set_current_commit(self, hexstr):
        self.previous_commit = self.current_commit
        self._set_to_datastore('previous_commit', self.previous_commit)
        self.current_commit = hexstr
        self._set_to_datastore('current_commit', self.current_commit)


    def on_repo_updated(self, git_repo):
        raise NotImplemented()
