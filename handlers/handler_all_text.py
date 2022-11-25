from handlers.handler import Handler
from settings import config
from settings.message import MESSAGES


class HandlerAllText(Handler):

    def __init__(self, bot):
        super().__init__(bot)
        self.step = None

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
            reply_markup=self.keyboards.remove_menu()
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

    def pressed_btn_product(self, message, product):
        self.bot.send_message(
            message.chat.id,
            f'Категория{config.KEYBOARD.get(product)}',
            reply_markup=self.keyboards.set_select_category(config.CATEGORY.get(product))
        )
        self.bot.send_message(
            message.chat.id,
            'Ok',
            reply_markup=self.keyboards.category_menu()
        )

    def pressed_btn_order(self, message):
        self.step = 0

        count = self.BD.select_all_product_id()
        quantity = self.BD.select_order_quantity(count[self.step])

        self.send_message_order(count[self.step], quantity, message)

    def send_message_order(self, product_id, quantity, message):
        self.bot.send_message(
            message.chat.id,
            MESSAGES.get('order_number').format(self.step + 1),
            parse_mode='HTML',
        )
        self.bot.send_message(
            message.chat.id,
            MESSAGES.get('order').format(
                self.BD.select_single_product_name(product_id),
                self.BD.select_single_product_title(product_id),
                self.BD.select_single_product_price(product_id),
                self.BD.select_order_quantity(product_id)
            ),
            parse_mode='HTML',
            reply_markup=self.keyboards.orders_menu(self.step, quantity)
        )

    def pressed_btn_up(self, message):
        count = self.BD.select_all_product_id()  # список всех товаров в заказе
        quantity_order = self.BD.select_order_quantity(count[self.step])  # количество конкретной позиции в заказе
        quantity_product = self.BD.select_single_product_quantity(count[self.step])  # кол-во продукта на складе

        if quantity_product > 0:
            quantity_order += 1
            quantity_product -= 1

            self.BD.update_order_value(count[self.step], 'quantity', quantity_order)
            self.BD.update_product_value(count[self.step], 'quantity', quantity_product)

        self.send_message_order(count[self.step], quantity_order, message)

    def pressed_btn_down(self, message):
        count = self.BD.select_all_product_id()
        quantity_order = self.BD.select_order_quantity(count[self.step])
        quantity_product = self.BD.select_single_product_quantity(count[self.step])

        if quantity_order > 0:
            quantity_order -= 1
            quantity_product += 1

            self.BD.update_order_value(count[self.step], 'quantity', quantity_order)
            self.BD.update_product_value(count[self.step], 'quantity', quantity_product)

        self.send_message_order(count[self.step], quantity_order, message)

    def pressed_btn_x(self, message):
        pass


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

            if message.text == config.KEYBOARD.get('ORDER'):
                if self.BD.count_rows_order() > 0:
                    self.pressed_btn_order(message)
                else:
                    self.bot.send_message(
                        message.chat.id,
                        MESSAGES['no_orders'],
                        parse_mode='HTML',
                        reply_markup=self.keyboards.category_menu()
                    )

            # Меню товаров
            if message.text == config.KEYBOARD.get('SEMI_PRODUCT'):
                self.pressed_btn_product(message, 'SEMI_PRODUCT')

            if message.text == config.KEYBOARD.get('GROCERY'):
                self.pressed_btn_product(message, 'GROCERY')

            if message.text == config.KEYBOARD.get('ICE_CREAM'):
                self.pressed_btn_product(message, 'ICE_CREAM')

            # Меню заказа
            if message.text == config.KEYBOARD.get('UP'):
                self.pressed_btn_up(message)

            if message.text == config.KEYBOARD.get('DOWN'):
                self.pressed_btn_down(message)

            if message.text == config.KEYBOARD.get('X'):
                self.pressed_btn_x(message)

            if message.text == config.KEYBOARD.get('BACK_STEP'):
                self.pressed_btn_back_step(message)

            if message.text == config.KEYBOARD.get('NEXT_STEP'):
                self.pressed_btn_next_step(message)

