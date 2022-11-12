from settings.config import KEYBOARD, VERSION, AUTHOR


trading_store = """
<b>Добро пожаловать в приложение
    IRON_DATA store</b>
"""


no_orders = """
<b>Заказ отсутствует</b>
"""


settings = """
<b>Общее руководство пользования</b>

<i>Навигация</i>

-<b>({})  - </b><i>назад</i>
-<b>({})  - </b><i>вперед</i>
-<b>({})  - </b><i>увеличить</i>
-<b>({})  - </b><i>уменьшить</i>
-<b>({})  - </b><i>следующий</i>
-<b>({})  - </b><i>предыдущий</i>

<i>Специальные кнопки:</i>

-<b>({})  - </b><i>удалить</i>
-<b>({})  - </b><i>заказ</i>
-<b>({})  - </b><i>Оформить заказ</i>

<i>Общая инф-ия:</i>

-<b>версия программы  - </b><i>{}</i>
-<b>разработчик  - </b><i>{}</i>

<b>Ваше имя</b>
""".format(
    KEYBOARD['<<'],
    KEYBOARD['>>'],
    KEYBOARD['UP'],
    KEYBOARD['DOWN'],
    KEYBOARD['NEXT_STEP'],
    KEYBOARD['BACK_STEP'],
    KEYBOARD['X'],
    KEYBOARD['ORDER'],
    KEYBOARD['APPLY'],
    VERSION,
    AUTHOR,
    KEYBOARD['COPY'],
)


app_lay = """
<b>Ваш заказ оформлен.</b>

<i>Общая стоимость - </i> <b>{} руб.</b>

<i>Общее кол-во позиций - </i> <b>{} ед.</b>
"""

product_order = """
Выбранный товар:

{}
{}
Стоимость заказа: {} руб.

На складе осталось {} ед.
"""

order = """

<i>Название
"""


MESSAGES = {
    'trading_store': trading_store,
    'settings': settings,
    'app_lay': app_lay,
    'no_orders': no_orders,
    'product_order': product_order,
    'order': order,
}
