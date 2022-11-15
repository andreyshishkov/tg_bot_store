from os import path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_base.dbcore import Base

from settings import config
from models.product import Products


class DBManager:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.engine = create_engine(config.DATABASE)
        self._session = sessionmaker(bind=self.engine)()

        if not path.isfile(config.DATABASE):
            Base.metadata.create_all(self.engine)

    def select_all_products_category(self, category):
        result = self._session.query(Products).filter_by(
            category_id=category
        ).all()
        self.close()
        return result

    def close(self):
        self._session.close()



