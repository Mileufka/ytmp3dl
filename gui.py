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
        self.button_dl = Button(master=self.bottom_frame,text="Download",fg="black",relief=GROOVE)
        self.button_add = Button(master=self.bottom_frame,text="Add",fg="black",command=self.add_panel,relief=GROOVE)
        

        self.nb_panel = 0
        self.panel_set = set()

        self.scrollable_frame.bind("<Configure>",lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.scrollable_frame_id = self.canvas.create_window((0, 0), window=self.scrollable_frame,anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.bind('<Configure>', self._configure_canvas)

        self.top_frame.pack(anchor=N,side=TOP,fill=X,expand=False)
        self.mid_frame.pack(anchor=N,side=TOP,fill=BOTH,expand=True)
        self.canvas.pack(anchor=W,side=LEFT,fill=BOTH,expand=True)
        self.scrollbar.pack(anchor=E,side=RIGHT,fill=Y,expand=False)
        self.bottom_frame.pack(anchor=S,side=BOTTOM,fill=X,expand=False)
        self.button_quit.pack(anchor=N,side=RIGHT, padx=2)
        self.button_dl.pack(anchor=N,side=RIGHT, padx=2)
        self.button_add.pack(anchor=N,side=RIGHT, padx=2)
        

    def close_window(self):
        self.master.destroy()

    def add_panel(self):
        self.panel_set.add(Panel_frame(master=self.scrollable_frame,nb=self.nb_panel))
        self.nb_panel += 1

    def _configure_canvas(self,event):
        """
        Used to correct panel_frames width
        """
        if self.scrollable_frame.winfo_reqwidth() != self.canvas.winfo_width():
            # update the inner frame's width to fill the canvas
            self.canvas.itemconfigure(self.scrollable_frame_id, width=self.canvas.winfo_width())
        

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
        self.label_year = Label(master=self,text='Year:')
        self.year = Entry(master=self)
        self.label_composer = Label(master=self,text='Composer:')
        self.composer = Entry(master=self)
        self.button_gen_filename = Button(master=self,text="Generate filename",fg="black",command=self.generate_filename,relief=GROOVE)
        self.label_filename = Label(master=self,text='Filename:')
        self.filename = Entry(master=self)
        self.button_del = Button(master=self,text="X",fg="red",command=self.del_panel,relief=GROOVE)

        self.pack(anchor=NW,side=TOP,fill=X,expand=True)

        self.label_url.grid(row=0,padx=2,pady=2,sticky=W)
        self.url.grid(row=0,column=1,padx=2,pady=2,columnspan=3,sticky=W+E)
        self.button_del.grid(row=0,column=4,rowspan=5,padx=2,pady=2,sticky=N+S+E)
        self.label_artist.grid(row=1,column=0,padx=2,pady=2,sticky=W)
        self.artist.grid(row=1,column=1,padx=2,pady=2,sticky=W+E)
        self.label_track.grid(row=1,column=2,padx=2,pady=2,sticky=W)
        self.track.grid(row=1,column=3,padx=2,pady=2,sticky=W+E)
        self.button_gen_filename.grid(row=2,column=1,pady=1,sticky=W)
        self.label_year.grid(row=2,column=2,padx=2,pady=2,sticky=W)
        self.year.grid(row=2,column=3,padx=2,pady=2,sticky=W+E)
        self.label_composer.grid(row=3,column=2,padx=2,pady=2,sticky=W)
        self.composer.grid(row=3,column=3,padx=2,pady=2,sticky=W+E)
        self.label_filename.grid(row=4,column=0,padx=2,pady=10,sticky=W)
        self.filename.grid(row=4,column=1,padx=2,pady=10,columnspan=3,sticky=W+E)
        

        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=0)
        self.grid_rowconfigure(3,weight=1)
        self.grid_rowconfigure(4,weight=1)
        self.grid_columnconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=0)
        self.grid_columnconfigure(3,weight=1)
        self.grid_columnconfigure(4,weight=0)

    def del_panel(self):
        self.destroy() 

    def generate_filename(self):
        fn = self.artist.get().replace(" ","_") + "_-_" + self.track.get().replace(" ","_")
        self.set_filename_entry_text(text=fn)
        
    def set_filename_entry_text(self,text):
        self.filename.delete(0,END)
        self.filename.insert(0,text)
        
