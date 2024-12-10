from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Стоимость'),
            KeyboardButton(text='О нас')
        ]
    ], resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Игра для новичков', callback_data='medium')],
        [InlineKeyboardButton(text='Игра для любителей', callback_data='big')],
        [InlineKeyboardButton(text='Игра для профессионалов', callback_data='mega')],
        [InlineKeyboardButton(text='Другие предложения', callback_data='other')]
    ]
)


buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Купить!', url='http://ya.ru')]
    ]
)