import logging

class RepoProjectBase(object):

    name = None

    repo_mirror_path = None
    repo_branch = None
    project_path = None

    current_commit = None
    previous_commit = None

    app = None
    datastore = None
    logger = None

    def __init__(self, app):
        self.app = app
        self.name = type(self).__name__
        self.datastore = app.datastore
        self.logger = logging.getLogger(type(self).__name__)

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


    def custom_trigger(self):
        return False
