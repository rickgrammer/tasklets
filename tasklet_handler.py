import utils
from tasklet import Tasklet, Store

class TaskletHandler:
    def __init__(self, parsed_args):
        self.parsed_args = parsed_args.__dict__
        self.store = Store()

    def handle_create(self):
        tasklet = Tasklet(**self.parsed_args)
        store.push(tasklet)

    def handle_edit(self):
        pass

    def handle_list(self):
        pass

    def handle_delete(self):
        pass

    def handle_tasklet(self):

        if self.parsed_args[action] == 'create':
            self.parsed_args[when] = utils.parse_datetime(parsed_args[when])
            self.handle_create()
        elif self.parsed_args[action] == 'edit':
            pass
        elif self.parsed_args[action] == 'list':
            pass
        elif self.parsed_args[action] == 'delete':
            pass
        else:
            exit('tasklet: %s is not supported. Actions supported: (create, edit, list, delete)' % action)
    
    def run(self):
        handle_tasklet()
