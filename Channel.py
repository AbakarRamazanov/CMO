import time
from threading import Thread


class Channel(Thread):
    report_manager_is_empty = 0
    request = 0
    flag = True
    flag_request = False

    def __init__(self, report_manager_is_empty):
        Thread.__init__(self)
        self.report_manager_is_empty = report_manager_is_empty
        pass

    def set_request(self, request):
        # print(self.get_name() + " get request is " + str(request.time_request) + " complexity")
        self.flag_request = True
        self.request = request

    def run(self):
        while self.flag:
            while self.flag_request:
                time.sleep(self.request.time_request)
                self.request.time_request = 0
                self.report_manager_is_empty(self)
                self.flag_request = False
            pass

    def channel_free(self):
        pass

    def remove_channel(self):
        self.flag = False
        pass

    name = "Channel#"

    def set_name(self, name):
        self.name += str(name)
        pass

    def get_name(self):
        return self.name
