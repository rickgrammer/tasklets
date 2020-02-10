import os
import gzip
import io
import datetime 
import random
import string
import functools

class Tasklet:
    '''
    priority: 5, 4, 3, 2, 1, 0 ; 0 being the highest priority
    status: created, paused, finished, running.
    '''
    def __init__(self,
            name,
            description='<No Description>',
            tag='general',
            priority=3,
            deadline=None,
            start_time=None,
            end_time=None
            ):
        self.id = self._create_task_id()
        self.name = name
        self.description = description
        self.tag = tag
        self.priority = priority
        self.deadline = deadline
        self.expected_time = expected_time
        self.start_time = start_time
        self.end_time = end_time
        self.status = 'created'
        self.is_finished = False

    def start_tasklet(self):
        this.start_time = datetime.datetime.now()
        # push to task list

    def end_tasklet(self):
        self.end_time = datetime.datetime.now()
        self.is_finished = True

    def change_tasklet_status(status):
        self.status = status

    @property
    def time_taken(self):
        if self.is_finished:
            return self.end_time - self.start_time
        return 'Task is not yet finished.'

    def _create_tasklet_id(self):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(20))
    
class Store:
    '''
        A centralised store where each tasklet is gziped and stored.
    '''

    def __init__(self, store_path=None):
        if not store_path:
            store_path = '/opt/tasklets/'
            os.makedirs(store_path)
        store_path += 'store.tsk'
        self._store_path = self.store_path

    def create_path_if_not_exists(func):
        '''
            Purpose: Incase the user deleted the store; decorator recreates it.
        '''
        @functools.wraps(func)
        def inner(*args, **kwargs):
            if not os.path.isfile(self._store_path):
                path, file = self._store_path.rsplit(os.path.sep, 1)
                os.makedirs(path)
            return func(*args, **kwargs)
        return inner


    @create_path_if_not_exists
    def _push_tasklet(self, compressed_tasklet):
        with gzip.open(self._store_path, 'a') as consumer:
            consumer.write(compressed_tasklet)

    def push_tasklet(self, tasklet):
        compressed_tasklet = gzip.compress(repr(tasklet).encode())
        self._push_tasklet(compressed_tasklet)

    def get_tasklets(id=None):
        with gzip.open(self._store_path, 'rb') as store_fp:
            tasklets=eval(store_fp.read().decode())
            if not id:
                return tasklets
            else:
                for tasklet in tasklets:
                    if tasklet.id == id: return tas
        raise Exception(id + ' not found.')


