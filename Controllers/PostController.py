from Models.Post import *

class PostController:
    '''
    создать(добавить),
    редактировать,
    удалить,
    показать популярные.
    '''
    @classmethod
    def add(cls, title, content, author, created_date, views):
        # Добавить пост в таблицу
        try:
            Post.create(
            title = title,
            content = content,
            author = author,
            created_date = created_date,
            views = views
            )
        except:
            print("Ошибка добавления пользователя")
    @classmethod
    def get(cls):
        # Выводит список записей из таблицы БД
        return Post.select()

    @classmethod
    def update_title(cls, id, title):
        # Обновить запись по id
        Post.update({Post.title:title}).where(Post.id == id).execute()

    @classmethod
    def update_all(cls, id, **kwargs):
        Post.update(**kwargs).where(Post.id == id).execute()

    @classmethod
    def search_views(cls,views):
        request = Post.select().where(Post.views == views) # Переменной передаём список записей у которых в поле views есть views из аргумента метода
        return request

    @classmethod
    def delete(cls, id):
        # Удалить пост по - id
        Post.delete_by_id(id)

if __name__ == "__main__":
    PostController.add(
        title="Новости Python",
        content="Последние новости...",
        author="Разработчик",
        created_date="2024-03-02",
        views=42
    )
    # PostController.update_title(2,'Блог о python')
    # PostController.update_all(1, author='Максим')

    for item in PostController.get():
        print(item.name, item.name)

    print(PostController.search_views(""))
    # PostController.delete(2)