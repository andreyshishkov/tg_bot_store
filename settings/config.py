from dotenv import load_dotenv
import os
from emoji import emojize

load_dotenv()

TOKEN = os.environ.get('TOKEN')
AUTHOR = 'User'
NAME_DB = 'products.sqlite'
VERSION = '0.0.1'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join('sqlite:///' + BASE_DIR, NAME_DB)

COUNT = 0

KEYBOARD = {
    'CHOOSE GOODS': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(':speech_balloon: О магазине'),
    'SETTINGS': emojize('Настройки'),
    'SEMI PRODUCT': emojize(':pizza: Полуфабрикаты'),
    'GROCERY': emojize(':bread: Бакалея'),
    'ICE CREAM': emojize(':shaved_ice: Мороженное'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('🔙'),
    'NEXT_STEP': emojize('➡'),
    'ORDER': emojize('✅ Заказ'),
    'X': emojize('❌'),
    'AMOUNT PRODUCT': COUNT,
    'AMOUNT ORDERS': COUNT,
    'UP': emojize(' ▲ '),
    'DOWN': emojize(' ▼ '),
    'APPLY': emojize('✅ Сделать заказ'),
    'COPY': emojize('©')
}

CATEGORY = {
    'SEMI PRODUCT': 1,
    'GROCERY': 2,
    'ICE CREAM': 3
}

COMMANDS = {
    'START': 'start',
    'HELP': 'help',
}
