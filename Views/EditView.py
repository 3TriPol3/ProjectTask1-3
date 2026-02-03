from tkinter import *
from tkinter import ttk

from Controllers.PostController import *


class EditView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Редактирование содержания поста")
        self.geometry("1280x920")

        self.label_frame = ttk.Frame(self,padding=[20])
        self.label_frame.pack(anchor=CENTER,pady=10,padx=10)

        self.label = ttk.Label(self.label_frame, text="Редактировать содержание поста")
        self.label.pack()

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
        # Превращает объекты из БД в список кортежей для таблицы
        self.table()
        # Для события выбора строки из таблицы вызову метод row_selected
        self.table_data.bind("<<TreeviewSelect>>", self.row_selected)
        # Редактирование содержания поста
        self.edit_frame = ttk.Frame(self,padding=[20])
        self.edit_frame.pack(anchor=CENTER, padx=10,pady=10)

        self.edit_title_label = ttk.Label(self.edit_frame, text="Название поста")
        self.edit_title_label.grid(row=1, column=0)
        self.edit_title_entry = ttk.Entry(self.edit_frame)
        self.edit_title_entry.grid(row=2, column=0)

        self.edit_title_button = ttk.Button(self.edit_frame, text="Редактировать", command=self.update_titl)
        self.edit_title_button.grid(row=2, column=2, padx=15)

        self.edit_content_label = ttk.Label(self.edit_frame,text="Содержание поста")
        self.edit_content_label.grid(row=3, column=0)
        self.edit_content_entry = ttk.Entry(self.edit_frame)
        self.edit_content_entry.grid(row=4,column=0)

        self.edit_title_button = ttk.Button(self.edit_frame, text="Редактировать", command=self.update_cont)
        self.edit_title_button.grid(row=4, column=2, padx=15)

        # Кнопка закрытия окна / перехода в главное
        # переход на главное окно
        self.button_move = ttk.Button(self, text="Вернуться на главную страницу", command=self.move)
        self.button_move.pack(anchor=CENTER)

    # Для обновления данных в таблице создал метод добавления записей из БД
    def table(self):
        # Очистить старые записи
        for item in self.table_data.get_children():
            self.table_data.delete(item)

        self.elemnt = []
        for el in PostController.get():
            self.elemnt.append(
                (el.id, el.title, el.content, el.author, el.created_date, el.views)
            )

        # Вывод данных из БД в таблицу
        for item in self.elemnt:
            self.table_data.insert("", END, values=item)
        self.table_data.pack()
    def row_selected(self, event):
        '''
        Метод передаст данные о выбранной записи - > передаст строку
        :return:
        '''
        # С помощью метода selection() self.row передаётся список из одной строки / [('id,name,...')]
        # Выделить одну строку можно с помощью [0] - индекса
        # Получить выбранные строки
        selected = self.table_data.selection()

        # Проверить, если строки не выбранны
        if not selected:
            return # Завершить работу метода

        self.row = self.table_data.selection()[0]

        self.id = self.table_data.item(self.row, "values")[0]
        return self.id

    def update_cont(self):
        PostController.update_content(id = self.id, content=self.edit_content_entry.get())
        self.table()

    def update_titl(self):
        PostController.update_title(id=self.id, title=self.edit_title_entry.get())
        self.table()

    def move(self):
        from Views.PostView import PostView
        window_home = PostView()
        self.destroy()

if __name__ == "__main__":
    win = EditView()
    win.mainloop()