#  настройки для подключения к базе данных
from databases import Database
from sqlalchemy import create_engine, MetaData
from core.config import DATABASE_URL

database = Database(DATABASE_URL)  # создали connection  к базе
metadata = MetaData()  # создали экземпляр класса Metadata  для создания таблиц
engine = create_engine(
    DATABASE_URL,
)  # для создания синхронных запросов к базе, создание таблиц нашего приложения на начальном этапе
