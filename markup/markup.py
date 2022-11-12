from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from settings import config
from data_base.dbalchemy import DBManager


class Keyboards:
    """
    For creating of interface of bot
    """

    def __init__(self):
        self.markup = None
        self.DB = DBManager()

    @staticmethod
    def set_btn(name, step=0, quantity=0):
        return KeyboardButton(config.KEYBOARD.get(name))

    def start_menu(self):
        """
        Создает разметку в основном меню
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('CHOOSE GOODS')
        itm_btn_2 = self.set_btn('INFO')
        itm_btn_3 = self.set_btn('SETTINGS')

        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2,itm_btn_3)
        return self.markup

    def info_menu(self):
        """
        Создает разметку в меню info
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn = self.set_btn(
            '<<'
        )
        self.markup.row(itm_btn)
        return self.markup

    def settings_menu(self):
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        self.markup.row(itm_btn_1)
        return self.markup
