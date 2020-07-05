#!/usr/bin/python3
#gui.py

from tkinter import *

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x700")
        self.main_frame = Main_frame(self)

    def close_window(self):
        self.destroy()

class Main_frame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(side=TOP,fill=BOTH,padx=5,expand=True)

        self.sub_frame = Frame(master=self,borderwidth=2,bg='white',relief=GROOVE)
        self.sub_frame.pack(anchor=N,side=TOP,fill=BOTH,expand=True)

        self.bottom_frame = Frame(master=self)
        self.bottom_frame.pack(anchor=S,side=BOTTOM,fill=X,expand=False)

        self.button_quit = Button(master=self.bottom_frame, text="Close", fg="red", command=self.close_window, relief=GROOVE)
        self.button_quit.pack(anchor=N,side=RIGHT, padx=2)

        self.button_add = Button(master=self.bottom_frame, text="Add", fg="black", command=self.add_panel, relief=GROOVE)
        self.button_add.pack(anchor=N,side=RIGHT, padx=2)

        self.panel_set = set()
        self.nb_panel = 0

    def close_window(self):
        self.master.destroy()

    def add_panel(self):
        self.nb_panel += 1
        self.panel_set.add(Panel_frame(master=self.sub_frame,nb=self.nb_panel))

class Panel_frame(Frame):
    def __init__(self, master=None, nb=0):
        super().__init__(master,height=100,borderwidth=2,relief=GROOVE)
        self.master = master
        self.nb = nb
        self.pack(anchor=N,side=TOP,fill=X,expand=False)
        self.label_url = Label(master=self,text='URL:')
        self.url = Entry(master=self)
        self.label_artist = Label(master=self,text='Artist:')
        self.artist = Entry(master=self)
        self.label_track = Label(master=self,text='Track:')
        self.track = Entry(master=self)

        self.label_url.pack(anchor=N,side=LEFT,padx=2)
        self.url.pack(anchor=N,side=LEFT,padx=2)
        self.label_artist.pack(anchor=S,side=LEFT,padx=2)
        self.artist.pack(anchor=S,side=LEFT,padx=2)
        self.label_track.pack(anchor=S,side=LEFT,padx=2)
        self.track.pack(anchor=S,side=LEFT,padx=2)
