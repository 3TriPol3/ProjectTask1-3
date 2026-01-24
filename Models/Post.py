from Models.Base import *

class Post(BaseModel):
    '''
    Данный класс описывает таблицу в БД с постами
    '''
    id = PrimaryKeyField() # id
    title = CharField(unique=True) # Название
    content = CharField() # Содержание
    author = CharField() # Автор
    created_date = DateField() # Дата создания
    views = CharField() # Количество просмотров


if __name__ == "__main__":
    mysql_db.create_tables([Post])
