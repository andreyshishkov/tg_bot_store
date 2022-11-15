from handlers.handler import Handler
from settings import config
from settings.message import MESSAGES


class HandlerAllText(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_info(self, message):
        self.bot.send_message(
            message.chat.id,
            MESSAGES['trading_store'],
            parse_mode='HTML',
            reply_markup=self.keyboards.info_menu(),
        )

    def pressed_btn_category(self, message):
        self.bot.send_message(
            message.chat.id,
            'Каталог категорий товаров',
            reply_markup=self.keyboards.remove_menu(),
        )
        self.bot.send_message(
            message.chat.id,
            'Сделайте свой выбор',
            reply_markup=self.keyboards.category_menu()
        )

    def pressed_btn_settings(self, message):
        self.bot.send_message(
            message.chat.id,
            MESSAGES['settings'],
            parse_mode='HTML',
            reply_markup=self.keyboards.settings_menu()
        )

    def pressed_btn_back(self, message):
        self.bot.send_message(
            message.chat.id,
            'Вы вернулись назад',
            reply_markup=self.keyboards.start_menu()
        )

    def handle(self):

        @self.bot.message_handler()
        def handle(message):

            # Основное меню
            if message.text == config.KEYBOARD.get('CHOOSE GOODS'):
                self.pressed_btn_category(message)

            if message.text == config.KEYBOARD.get('INFO'):
                self.pressed_btn_info(message)

            if message.text == config.KEYBOARD.get('SETTINGS'):
                self.pressed_btn_settings(message)

            if message.text == config.KEYBOARD.get('<<'):
                self.pressed_btn_back(message)

            # Меню товаров
            if message.text == config.KEYBOARD.get('SEMI PRODUCT'):
                self.pressed_btn_product(message, 'SEMI PRODUCT')

            if message.text == config.KEYBOARD.get('GROCERY'):
                self.pressed_btn_product(message, 'GROCERY')

            if message.text == config.KEYBOARD.get('ICE CREAM'):
                self.pressed_btn_product(message, 'ICE CREAM')
