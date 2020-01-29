import datetime 
import random
import string

class Task:
    '''
    priority: 5, 4, 3, 2, 1, 0 ; 0 being the highest priority
    '''
    def __init__(self,
            title,
            description='<No Description>',
            tag='general',
            priority=3,
            deadline=None,
            expected_time=None,
            start_time=None,
            end_time=None
            ):
        self.id = self._create_task_id()
        self.title = title
        self.description = description
        self.tag = tag
        self.priority = priority
        self.deadline = deadline
        self.expected_time = expected_time
        self.start_time = start_time
        self.end_time = end_time
        self.is_finished = False

    def start_task(self):
        this.start_time = datetime.datetime.now()
        # push to task list

    def end_task(self):
        self.end_time = datetime.datetime.now()
        self.is_finished = True

    @property
    def time_taken(self):
        if self.is_finished:
            return self.end_time - self.start_time
        return 'Task is not yet finished.'

    def _create_task_id(self):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(20))
    

