import threading

import Channel


class ChannelManager(object):
    event_channel_manager = threading.Event()
    empty_channels = list()
    total_channels = 0
    dead_requests = 0

    def __init__(self, number_of_channels):
        self.total_channels = 0
        self.dead_requests = 0
        self.create_channels(number_of_channels)
        # self.event_channel_manager.set()

    def add_channel(self, ev):
        # self.event_channel_manager.wait()
        # self.event_channel_manager.clear()
        channel = Channel.Channel(self.channel_is_empty)
        channel.set_name(self.cng())
        channel.start()
        self.empty_channels.append(channel)
        self.total_channels += 1
        # self.event_channel_manager.set()

    def remove_channel(self, ev):
        # self.event_channel_manager.wait()
        # self.event_channel_manager.clear()
        self.empty_channels.pop().remove_channel()
        self.total_channels -= 1
        # self.event_channel_manager.set()

    def get_stat(self):
        return "Всего каналов = " + str(self.total_channels) + ". Занято каналов = " + str(
            self.total_channels - len(self.empty_channels)) + ". Свободно каналов = " + str(
            len(self.empty_channels))
        pass

    def get_request(self, request):
        # print("get_request")
        # self.event_channel_manager.wait()
        # self.event_channel_manager.clear()
        if self.empty_channels:
            channel = self.empty_channels.pop()
            channel.set_request(request)
        else:
            self.dead_requests += 1
        # self.event_channel_manager.set()
        pass

    def channel_is_empty(self, channel):
        # print(str(channel.get_name()) + " is empty")
        # self.event_channel_manager.wait()
        # self.event_channel_manager.clear()
        self.empty_channels.append(channel)
        # self.event_channel_manager.set()
        pass

    def create_channels(self, number_of_channels):
        # self.event_channel_manager.wait()
        # self.event_channel_manager.clear()
        while number_of_channels:
            self.add_channel(5)
            number_of_channels -= 1
        # print("first create channel")
        # self.event_channel_manager.set()

    cngn = 0

    def cng(self):
        self.cngn += 1
        return self.cngn
