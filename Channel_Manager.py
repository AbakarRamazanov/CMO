from threading import Thread

import Channel


class Channel_Manager(Thread):
    # requests_manager = 0
    get_part_requests = 0
    channels = list()
    channels_empty = list()

    def __init__(self, name_def_get_part_requests, start_count_channel=3):
        Thread.__init__(self)
        # self.requests_manager = requests_manager
        self.get_part_requests = name_def_get_part_requests
        for n in range(start_count_channel):
            channel = Channel.Channel()
            channel.start()
            self.channels_empty.append(channel)

    def run(self):
        while True:
            self.count_empty_channel()
            if len(self.channels_empty):
                requests = self.get_part_requests(len(self.channels_empty))
                while len(requests):
                    # self.channels[0].stop()
                    self.channels_empty[0].put_request(requests.pop())
                    self.channels.append(self.channels_empty.pop(0))
                    pass
            pass

    def count_empty_channel(self):
        count = 0
        # print(len(self.channels))
        while not count >= len(self.channels):
            if self.channels[count].is_empty():
                self.channels_empty.append(self.channels.pop(count))
                pass
            else:
                count = count + 1

    def create_new_channel(self, ev):
        self.channels_empty.append(Channel.Channel())
        pass

    def remove_channel(self, ev):
        if len(self.channels_empty) > 0:
            self.channels_empty.pop()
        pass

    def get_stat(self):
        return "Всего каналов = " + str(len(self.channels_empty) + len(self.channels)) + ". Занято каналов = " + str(
            len(self.channels)) + ". Свободно каналов = " + str(len(self.channels_empty))

        # return {"Всего каналов": len(self.channels_empty) + len(self.channels),
        #         "Занято каналов": len(self.channels),
        #         "Свободно каналов": len(self.channels_empty)}
        pass


if __name__ == '__main__':
    import Request_Manager

    requester = Request_Manager.Request_Manager()
    channel_manager = Channel_Manager(name_def_get_part_requests=requester.get_part, start_count_channel=3)
    requester.start()
    channel_manager.start()
    pass
