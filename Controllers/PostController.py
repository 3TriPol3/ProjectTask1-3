from Models.Post import *

class PostController:
    '''
    создать(добавить),
    редактировать,
    удалить,
    показать популярные.
    '''

    # Добавить пост в таблицу
    @classmethod
    def add(cls, title, content, author, created_date, views):
        try:
            Post.create(
            title = title,
            content = content,
            author = author,
            created_date = created_date,
            views = views
            )
        except:
            print("Ошибка добавления поста")

    # Выводит список записей из таблицы БД
    @classmethod
    def get(cls):
        return Post.select()

    # Изменить название по id
    @classmethod
    def update_content(cls, id, content):
        Post.update({Post.content:content}).where(Post.id == id).execute()

    # Редактирование
    @classmethod
    def update_all(cls, id, **kwargs):
        Post.update(**kwargs).where(Post.id == id).execute()

    # Удалить пост по - id
    @classmethod
    def delete(cls, id):
        Post.delete_by_id(id)

    @classmethod
    def search_views(cls,views):
        request = Post.select().where(Post.views == views) # Переменной передаём список записей у которых в поле views есть views из аргумента метода
        return request

    # Поиск самых популярных постов
    # Сортировка
    # @classmethod
    # def sorted(cls):
    #     Post.select().order_by(Post.views)

    @classmethod
    def sorted(cls, limit=10):
        return Post.select().order_by(Post.views.desc()).limit(limit)


if __name__ == "__main__":
    # PostController.add(   # Добавить пост в таблицу
    #     title="Мой 7 пост",
    #     content="Содержание 7",
    #     author="Пользователь 7",
    #     created_date="2020-01-01",
    #     views=9
    # )

    # PostController.update_title(2,'Блог о python') # Изменить название по id
    # PostController.update_all(1, author='Максим') # Редактирование

    # for item in PostController.get():  # Выводит список записей из таблицы БД
    #     print(item.title, item.content, item.author, item.created_date, item.views)

    # PostController.delete(4) # Удалить пост по - id


    # Получение топ-10 по views (убывание)
    top_posts = PostController.sorted(limit=10)
    print(PostController.sorted(limit=10))
    print(top_posts)
