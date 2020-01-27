import os
import gzip
import io

class Store:

    def __init__(self, store_path='/opt/tasklets/store.tsk'):
        self._store_path = self.store_path

    def _push_task(self, compressed_task):
        with gzip.open(self._store_path) as producer:
            with gzip.open('_tmp_store.tsk', 'wb') as consumer:
                self.__update_store(producer, consumer, compressed_task)
        os.rename('_tmp_store.tsk', self.store_path)

    def push_task(self, task):
        compressed_task = gzip.compress(repr(task).encode())
        self._push_task(compressed_task)

    def __update_store(producer, consumer, compressed_task):
        while True:
            produced = producer.read(1)
            if not produced: return
            consumer.write(produced)
        consumer.write(compressed_task)

