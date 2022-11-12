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
            reply_markup=self.keyboards.info_menu()
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

            if message.text == config.KEYBOARD.get('INFO'):
                self.pressed_btn_info(message)

            if message.text == config.KEYBOARD.get('SETTINGS'):
                self.pressed_btn_settings(message)

            if message.text == config.KEYBOARD.get('<<'):
                self.pressed_btn_back(message)
