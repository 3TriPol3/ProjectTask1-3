from tkinter import *
from tkinter import ttk
from Controllers.PostController import *

class PostView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Блог с постами")
        self.geometry("1280x920")

        # Фрейм Добавить пост
        self.add_frame = ttk.Frame(self,
                                   borderwidth=1,
                                   relief=SOLID,
                                   padding=[18], # внутренние отступы фрейма
        )
        self.add_frame.pack(
            anchor=CENTER,
            fill=X,
            padx=10,
            pady=10,
        )
        #Фрейм, в котором расположен текст Добавить Пост (Находится внутри фрейма add_frame)
        self.add_title_frame = ttk.Frame(self.add_frame,
                                         relief=SOLID,
                                         borderwidth=1,
                                         padding=[8, 10])
        self.add_title_frame.pack(anchor=CENTER,
                                  fill=X,
                                  padx=10,
                                  pady=10,
                                  )
        self.add_title = ttk.Label(self.add_title_frame, text="Добавить Пользователя")
        self.add_title.pack()
        # Фрейм в котором расположены окна ввода данных о Посте (Находится внутри фрейма add_frame)
        self.add_input_frame = ttk.Frame(self.add_frame,
                                         relief=SOLID,
                                         borderwidth=1,
                                         padding=[8, 10]
                                         )
        self.add_input_frame.pack(fill=X,
                                  padx=10,
                                  pady=10,
                                  )
        # Окна ввода данных Поста для добавления в таблицу БД
        self.add_title_title = ttk.Label(self.add_input_frame, text="Имя")
        self.add_title_title.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.add
