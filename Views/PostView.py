from tkinter import *
from tkinter import ttk
from Controllers.PostController import *

class PostView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("")
