from tkinter import *
from tkinter import ttk

from Controllers.PostController import *
from Views.DeleteView import DeleteView
from Views.EditView import EditView


class PostView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Блог с постами")
        self.geometry("1280x920")

        self.table_content = 0

        # Фрейм Добавить пост
        self.add_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[18], # внутренние отступы фрейма
        )
        self.add_frame.pack(anchor=CENTER, fill=X, padx=10, pady=10)

        #Фрейм, в котором расположен текст Добавить Пост (Находится внутри фрейма add_frame)
        self.add_title_frame = ttk.Frame(self.add_frame, relief=SOLID, borderwidth=1, padding=[8, 10])
        self.add_title_frame.pack(anchor=CENTER, fill=X, padx=10, pady=10,)

        self.add_title = ttk.Label(self.add_title_frame, text="Добавить пост")
        self.add_title.pack()

        # Фрейм в котором расположены окна ввода данных о Посте (Находится внутри фрейма add_frame)
        self.add_input_frame = ttk.Frame(self.add_frame, relief=SOLID, borderwidth=1, padding=[8, 10])
        self.add_input_frame.pack(fill=X, padx=10, pady=10)

        # Окна ввода данных Поста для добавления в таблицу БД
        self.add_title_title = ttk.Label(self.add_input_frame, text="Название")
        self.add_title_title.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.add_title_content= ttk.Label(self.add_input_frame, text="Содержание")
        self.add_title_content.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        self.add_title_author = ttk.Label(self.add_input_frame, text="Автор")
        self.add_title_author.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        self.add_title_created_date = ttk.Label(self.add_input_frame, text="Дата создания")
        self.add_title_created_date.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)

        self.add_title_views = ttk.Label(self.add_input_frame, text="Количество просмотров")
        self.add_title_views.grid(row=0, column=4, sticky="nsew", padx=5, pady=5)


        self.add_title = ttk.Entry(self.add_input_frame)
        self.add_title.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        self.add_content = ttk.Entry(self.add_input_frame)
        self.add_content.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        self.add_author = ttk.Entry(self.add_input_frame)
        self.add_author.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

        self.add_created_date = ttk.Entry(self.add_input_frame)
        self.add_created_date.grid(row=1, column=3, sticky="nsew", padx=5, pady=5)

        self.add_views = ttk.Entry(self.add_input_frame)
        self.add_views.grid(row=1, column=4, sticky="nsew", padx=5, pady=5)


        self.add_button = ttk.Button(self.add_input_frame, text="Добавить Пост", command=self.add_data)
        self.add_button.grid(row=1, column=5, sticky="nsew", padx=5, pady=5)

        self.add_button_sort = ttk.Button(self.add_input_frame, text="Показать популярные")
        self.add_button_sort.grid(row=1, column=6, sticky="nsew", padx=5, pady=5)

        # Фрейм Вывод Постов
        self.get_data = ttk.Frame(
            self,
            relief="raised",
            borderwidth=3,
            padding=[5]
        )
        self.get_data.pack(
            anchor=CENTER
        )
        # Фрейм Таблицы
        self.table_frame = ttk.Frame(self, padding=[20])
        self.table_frame.pack(anchor=CENTER, pady=10, padx=10)
        # Таблица
        self.columns = ('id', "title", 'content', 'author', 'created_date', 'views')  # Столбцы
        self.table_data = ttk.Treeview(self.table_frame, columns=self.columns, show='headings')
        # Заголовки
        self.table_data.heading('id', text="№")
        self.table_data.heading('title', text='Название')
        self.table_data.heading('content', text='Содержание')
        self.table_data.heading('author', text='Автор')
        self.table_data.heading('created_date', text='Дата создания')
        self.table_data.heading('views', text='Количество просмотров')
        # Для события выбора строки из таблицы вызову метод row_selected
        self.table_data.bind("<<TreeviewSelect>>", self.row_selected)
        # Превращает объекты из БД в список кортежей для таблицы
        self.table()
        # Фрейм для редактирования поста
        self.edit_frame = ttk.Frame(self, padding=[20])
        self.edit_frame.pack(anchor=CENTER, padx=5, pady=5)

        # Фрейм окна удаления постов
        self.delete_frame = ttk.Frame(self, padding=[20])
        self.delete_frame.pack(anchor=CENTER, padx=5, pady=5)

        # Кнопка перехода в окно удаления постов
        self.button_delete = ttk.Button(self.delete_frame, text="Удаление постов", command=self.delete_window)
        self.button_delete.grid(row=1, column=2, padx=5, sticky="s")

        # Кнопка перехода в окно редактирования постов
        self.update_content = ttk.Button(self.edit_frame, text="Редактировать пост", command=self.edit_window)
        self.update_content.grid(row=1, column=3, padx=5, sticky="s")

    def delete_window(self):
        window = DeleteView()
        self.destroy()

    def edit_window(self):
        window = EditView()
        self.destroy()

    # Для обновления данных в таблице создал метод добавления записей из БД
    def table(self):
        # Очистить старые записи
        for item in self.table_data.get_children():
            self.table_data.delete(item)

        self.elemnt = []
        for el in PostController.get():
            self.elemnt.append((el.id, el.title, el.content, el.author, el.created_date, el.views))
        # Вывод данных из БД в таблицу
        for item in self.elemnt:
            self.table_data.insert("", END, values=item)
        self.table_data.pack()

    def add_data(self):
        self.title = self.add_title.get()
        self.content = self.add_content.get()
        self.author = self.add_author.get()
        self.created_date = self.add_created_date.get()
        self.views = self.add_views.get()
        PostController.add(
            self.title,
            self.content,
            self.author,
            self.created_date,
            self.views
        )
        # Обновить данные таблицы Treeview
        self.table()
        # Очистить поля ввода
        self.clear()

    def clear(self):
        '''
        Метод очистит окна Treeview
        :return:
        '''
        self.add_title.delete(0, END)  # c 0-го идекса до конца
        self.add_content.delete(0, END)  # c 0-го идекса до конца
        self.add_author.delete(0, END)  # c 0-го идекса до конца
        self.add_created_date.delete(0, END)  # c 0-го идекса до конца
        self.add_views.delete(0, END)  # c 0-го идекса до конца

    def row_selected(self, event):
        selected = self.table_data.selection()
        # Проверить, если строки не выбранны
        if not selected:
            return  # Завершить работу метода
        self.row = self.table_data.selection()[0]
        self.id = self.table_data.item(self.row, "values")[0]
        return self.id

    # Для обновления данных в таблице создал метод добавления записей из БД
    def sort(self):
       for el in self.table_data.get_children():
           self.table_data.delete(el)
       if self.table_content == 0:
           self.mode = PostController.get()
       else:
           self.mode = PostController.sorted()
       lst = []
       for el in self.mode:
           lst.append(
               (el.id, el.title, el.content, el.author, el.created_date, el.views)
           )
       for el in lst:
            self.table_data.insert("", 'end', values=el)

    # def filter(self):
    #    if self.table_content == 0:
    #       self.table_content = 1
    #       self.add_button_sort['text'] = "По умолчанию"
    #       self.table()
    #    else:
    #       self.table_content = 0
    #       self.add_button_sort['text'] = "Популярное"
    #       self.table()


if __name__ == "__main__":
    window = PostView()
    window.mainloop()