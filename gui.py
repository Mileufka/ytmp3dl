#!/usr/bin/python3
#gui.py

from tkinter import *

class Main_frame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(side=TOP,fill=BOTH,padx=5,expand=True)
        
        self.top_frame = Frame(master=self)
        self.mid_frame = Frame(master=self)
        self.canvas = Canvas(master=self.mid_frame,borderwidth=2,bg='white',relief=GROOVE)
        self.scrollable_frame = Frame(master=self.canvas)
        self.scrollbar = Scrollbar(master=self.mid_frame,orient="vertical",command=self.canvas.yview)
        self.bottom_frame = Frame(master=self)
        self.button_quit = Button(master=self.bottom_frame,text="Close",fg="red",command=self.close_window,relief=GROOVE)
        self.button_add = Button(master=self.bottom_frame,text="Add",fg="black",command=self.add_panel,relief=GROOVE)

        self.nb_panel = 0
        self.panel_set = set()

        self.add_panel()

        self.scrollable_frame.bind("<Configure>",lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame,anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.top_frame.pack(anchor=N,side=TOP,fill=X,expand=False)
        self.mid_frame.pack(anchor=N,side=TOP,fill=BOTH,expand=True)
        self.canvas.pack(anchor=W,side=LEFT,fill=BOTH,expand=True)
        self.scrollbar.pack(anchor=E,side=RIGHT,fill=Y,expand=False)
        self.bottom_frame.pack(anchor=S,side=BOTTOM,fill=X,expand=False)
        self.button_quit.pack(anchor=N,side=RIGHT, padx=2)
        self.button_add.pack(anchor=N,side=RIGHT, padx=2)

        

    def close_window(self):
        self.master.destroy()

    def add_panel(self):
        self.panel_set.add(Panel_frame(master=self.scrollable_frame,nb=self.nb_panel))
        self.nb_panel += 1

class Panel_frame(Frame):
    def __init__(self, master=None, nb=0):
        super().__init__(master,height=100,borderwidth=2,relief=GROOVE)
        self.master = master
        self.nb = nb
        
        self.label_url = Label(master=self,text='URL:')
        self.url = Entry(master=self)
        self.label_artist = Label(master=self,text='Artist:')
        self.artist = Entry(master=self)
        self.label_track = Label(master=self,text='Track:')
        self.track = Entry(master=self)
        self.label_filename = Label(master=self,text='Filename:')
        self.filename = Entry(master=self)

        self.pack(anchor=NW,side=TOP,fill=X,expand=True)

        self.label_url.grid(row=0,padx=2,pady=2,sticky=W)
        self.url.grid(row=0,column=1,padx=2,pady=2,columnspan=3,sticky=W+E)
        self.label_artist.grid(row=1,column=0,padx=2,pady=2,sticky=W)
        self.artist.grid(row=1,column=1,padx=2,pady=2,sticky=W+E)
        self.label_track.grid(row=1,column=2,padx=2,pady=2,sticky=W)
        self.track.grid(row=1,column=3,padx=2,pady=2,sticky=W+E)
        self.label_filename.grid(row=2,column=0,padx=2,pady=10,sticky=W)
        self.filename.grid(row=2,column=1,padx=2,pady=10,columnspan=3,sticky=W+E)

        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)
        self.grid_columnconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=0)
        self.grid_columnconfigure(3,weight=1)

        
