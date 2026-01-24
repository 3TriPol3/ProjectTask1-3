from tkinter import *
from tkinter import ttk

from Controllers.PostController import *

class DeleteView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Удаление постов")
        self.geometry("1280x920")

        self.label_frame = ttk.Frame(self,padding=[20])
        self.label_frame.pack(anchor=CENTER,pady=10,padx=10)

        self.label = ttk.Label(self.label_frame, text="Удалить пост")
        self.label.pack()

        # Таблица
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
        self.delete_frame = ttk.Frame(self,padding=[20])
        self.delete_frame.pack(anchor=CENTER, padx=10,pady=10)

        self.delete_button = ttk.Button(self.delete_frame,text="Удалить Пост", command=self.delete_post)
        self.delete_button.grid(row=1,column=1, padx=15)

        # Кнопка закрытия окна / перехода в главное
        # переход на главное окно
        self.button_move = ttk.Button(self, text="Вернуться на главную страницу", command=self.move)
        self.button_move.pack(anchor=CENTER)

    # Метод добавления записей из БД
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
    def delete_post(self):
        PostController.delete(id = self.id)
        self.table()

    def move(self):
        from Views.PostView import PostView
        window_home = PostView()
        self.destroy()

if __name__ == "__main__":
    window = DeleteView()
    window.mainloop()



