from tkinter import *
from tkinter import ttk

from Controllers.PostController import *


class SortView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Самые популярные посты")
        self.geometry("1280x920")

        self.table_content = 0

        self.label_frame = ttk.Frame(self, padding=[20])
        self.label_frame.pack(anchor=CENTER, pady=10, padx=10)

        self.label = ttk.Label(self.label_frame, text="Показать популярные посты")
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
        # Удаление поста
        self.sort_frame = ttk.Frame(self, padding=[20])
        self.sort_frame.pack(anchor=CENTER, padx=10, pady=10)

        self.sort_button = ttk.Button(self.sort_frame, text="Показать самые популярные", command=self.filter)
        self.sort_button.grid(row=1, column=1, padx=15)

        # Кнопка закрытия окна / перехода в главное
        # переход на главное окно
        self.button_move = ttk.Button(self, text="Вернуться на главную страницу", command=self.move)
        self.button_move.pack(anchor=CENTER)


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
            self.table_data.insert("", END, values=el)

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


    def filter(self):
        if self.table_content == 0:
            self.table_content = 1
            self.sort_button['text'] = "По умолчанию"
            self.table()
        else:
            self.table_content = 0
            self.sort_button['text'] = "Показать самые популярные"
            self.table()

    def row_selected(self, event):
        selected = self.table_data.selection()
        if not selected:
            return # Завершить работу метода
        self.row = self.table_data.selection()[0]
        self.id = self.table_data.item(self.row, "values")[0]
        return self.id

    def move(self):
        from Views.PostView import PostView
        window_home = PostView()
        self.destroy()

if __name__ == "__main__":
    window = SortView()
    window.mainloop()