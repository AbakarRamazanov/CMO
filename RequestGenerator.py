import random
import time
import threading
from threading import Thread

import Request


# TODO исключения прописать
class RequestGenerator(Thread):
    func_send_request_channel_manager = 0
    intensity = 0

    def __init__(self, func_get_request=0, intensity=5):
        Thread.__init__(self)
        self.func_send_request_channel_manager = func_get_request
        self.intensity = intensity
        random.seed()
        pass

    def run(self):
        while True:
            time.sleep(random.randint(1, 2))
            self.func_send_request_channel_manager(Request.Request(random.randint(1, 10)))
            pass

    def set_func_send_request(self, func_get_request=0):
        self.func_send_request_channel_manager = func_get_request
        pass
