from tkinter import *
from threading import Thread

import Request_Manager
import Channel_Manager


class ThreadWindow(Thread):
    root = 0
    lbl = 0
    request_manager = 0
    channel_manager = 0
    stat_text = 0

    def __init__(self):
        Thread.__init__(self)
        self.request_manager = Request_Manager.Request_Manager()
        self.channel_manager = Channel_Manager.Channel_Manager(name_def_get_part_requests=self.request_manager.get_part,
                                                               start_count_channel=3)
        self.request_manager.start()
        self.channel_manager.start()

        self.root = Tk()
        btn_create_new_channel = Button(self.root, text='Add channel')
        btn_remove_empty_channel = Button(self.root, text='Remove channel')
        btn_create_new_channel.bind('<Button-1>', self.channel_manager.create_new_channel)
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

    def get_request_manager(self):
        return self.request_manager

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
