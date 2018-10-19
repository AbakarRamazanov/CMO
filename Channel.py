import time
import threading
from threading import Thread
import Request


class Channel(Thread):
    _processing_time = 0
    event = threading.Event()

    def __init__(self):
        Thread.__init__(self)
        self.event.set()
        self.event.wait()
        self.event.set()

    def put_request(self, request):
        self._processing_time = request.get_processing_time()
        pass

    def is_empty(self):
        if self.event.is_set():
            return True
        return False

    def run(self):
        while True:
            self.event.clear()
            try:
                while not self._processing_time <= 0:
                    time.sleep(1)
                    self._processing_time = self._processing_time - 1
            finally:
                self.event.set()