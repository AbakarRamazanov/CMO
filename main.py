from tkinter import *
from threading import Thread

import RequestGenerator
import ChannelManager


# if __name__ == '__main__':
#     channel_manager = ChannelManager.ChannelManager(3)
#     request_generator = RequestGenerator.RequestGenerator(channel_manager.get_request)
#     request_generator.start()
#     pass



class ThreadWindow(Thread):
    root = 0
    lbl = 0
    request_generator = 0
    channel_manager = 0
    stat_text = 0

    def __init__(self):
        Thread.__init__(self)
        self.channel_manager = ChannelManager.ChannelManager(3)
        self.request_generator = RequestGenerator.RequestGenerator(self.channel_manager.get_request)
        self.request_generator.start()

        # self.request_generator.start()
        # self.channel_manager.start()

        self.root = Tk()
        btn_create_new_channel = Button(self.root, text='Add channel')
        btn_remove_empty_channel = Button(self.root, text='Remove channel')
        btn_create_new_channel.bind('<Button-1>', self.channel_manager.add_channel)
        btn_remove_empty_channel.bind('<Button-1>', self.channel_manager.remove_channel)

        btn_create_new_channel.pack(side='left')
        btn_remove_empty_channel.pack(side='right')

        self.stat_text = StringVar()
        self.lbl = Label(self.root, textvariable=self.stat_text)
        self.lbl.pack(side='top')


    def run(self):
        self.root.mainloop()

    def get_channel_manager(self):
        return self.channel_manager

    def get_request_generator(self):
        return self.request_generator

    def get_root(self):
        return self.root

    def get_lbl(self):
        return self.lbl


thread_window = ThreadWindow()

thread_window.start()

channel_manager = thread_window.get_channel_manager()
lbl = thread_window.stat_text
root = thread_window.get_root()
while True:

    stat = channel_manager.get_stat()
    s = lbl.get()
    lbl.set(stat)
    # print(lbl.text)
    root.update()
    pass
