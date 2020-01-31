import os
import gzip
import io

class Store:
    '''
        A centralised store where each task is stored.
    '''

    def __init__(self, store_path='/opt/tasklets/store.tsk'):
        self._store_path = self.store_path

    def _push_task(self, compressed_task):
        with gzip.open(_store_path, 'a') as consumer:
            consumer.write(compressed_task)

    def push_task(self, task):
        compressed_task = gzip.compress(repr(task).encode())
        self._push_task(compressed_task)

    def get_tasks(id=None):
        with gzip.open(self._store_path, 'rb') as store_fp:
            tasks=eval(store_fp.read().decode())
            if not id:
                return tasks
            else:
                for task in tasks:
                    if task.id == id: return tas
        raise Exception(id + ' not found.')




