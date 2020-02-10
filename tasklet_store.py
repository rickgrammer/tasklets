import os
import gzip
import io

class Store:
    '''
        A centralised store where each tasklet is gziped and stored.
    '''

    def __init__(self, store_path='/opt/tasklets/store.tsk'):
        self._store_path = self.store_path

    def _push_tasklet(self, compressed_tasklet):
        with gzip.open(_store_path, 'a') as consumer:
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




