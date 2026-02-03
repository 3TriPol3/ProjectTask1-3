from tkinter import *
from tkinter import ttk

from Controllers.PostController import *

class SortView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Сортировка по популярности")
        self.geometry("1280x920")

        # Фрейм заголовка
        self.label_frame = ttk.Frame(self, padding=[20])
        self.label_frame.pack(anchor="center", pady=10)

        self.label = ttk.Label(self.label_frame, text="Сортировка по популярности")
        self.label.pack()

        # Таблица
        self.table_frame = ttk.Frame(self, padding=[20])
        self.table_frame.pack()

        self.columns = ('id', 'title', 'content', 'author', 'created_date', 'views')

        self.table_data = ttk.Treeview(self.table_frame, columns=self.columns, show='headings', height=15)

        # Заголовки таблицы
        self.table_data.heading('id', text='№')
        self.table_data.heading('title', text='Название')
        self.table_data.heading('content', text='Содержание')
        self.table_data.heading('author', text='Автор')
        self.table_data.heading('created_date', text='Дата создания')
        self.table_data.heading('views', text='Просмотры')

        # Для события выбора строки из таблицы вызову метод row_selected
        self.table_data.bind("<<TreeviewSelect>>", self.row_selected)

        # Кнопки управления
        self.button_frame = ttk.Frame(self, padding=[20])
        self.button_frame.pack(pady=10)

        self.sort_button = ttk.Button(self.button_frame, text="Сортировать по просмотрам", command=self.toggle_sort)
        self.sort_button.grid(row=0, column=0, padx=10)

        self.return_button = ttk.Button(self.button_frame, text="Закрыть окно", command=self.destroy)
        self.return_button.grid(row=0, column=1, padx=10)

        # Кнопка закрытия окна / перехода в главное
        # переход на главное окно
        self.button_move = ttk.Button(self, text="Вернуться на главную страницу", command=self.move)
        self.button_move.pack(anchor=CENTER)

        # Состояние: False — обычный порядок, True — отсортировано
        self.sorted = False

        # Загрузка данных
        self.table()

    def table(self):
        # Очистка таблицы
        for item in self.table_data.get_children():
            self.table_data.delete(item)
        try:
            if self.sorted:
                posts = PostController.sorted()  # Сортировка по views DESC
            else:
                posts = PostController.get()  # Без сортировки
            for el in posts:
                self.table_data.insert("", END, values=(
                    el.id,
                    el.title,
                    el.content,
                    el.author,
                    el.created_date,
                    el.views
                ))

            self.elemnt = []
            for item in self.elemnt:
                self.table_data.insert("", END, values=item)
            self.table_data.pack()
        except Exception as el:
            from tkinter.messagebox import showerror
            showerror("Ошибка", f"Не удалось загрузить данные: {el}")


    def toggle_sort(self):
        self.sorted = not self.sorted
        if self.sorted:
            self.sort_button.config(text="По умолчанию")
        else:
            self.sort_button.config(text="Сортировать по просмотрам")
        self.table()

    def row_selected(self, event):
        selected = self.table_data.selection()
        if not selected:
            return  # Завершить работу метода
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