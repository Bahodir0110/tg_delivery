from telebot import types

def num_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    num = types.KeyboardButton('Поделиться контактом', request_contact=True)
    kb.add(num)
    return kb

def loc_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    loc = types.KeyboardButton('Поделиться геопозицией', request_location=True)
    kb.add(loc)
    return kb

def remove():
    types.ReplyKeyboardRemove()

def main_menu_buttons(products_from_db):
    kb = types.InlineKeyboardMarkup(row_width=2)
    cart = types.InlineKeyboardButton(text='Корзина', callback_data='cart')
    all_products = [types.InlineKeyboardButton(text=f'{i[2]}', callback_data=i[1]) for i in products_from_db]
    kb.row(cart)
    kb.add(*all_products)

    return kb

def choose_product_count(current_amount=1, plus_or_minus=''):
    kb = types.InlineKeyboardMarkup(row_width=3)
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    plus = types.InlineKeyboardButton(text='+', callback_data='increment')
    minus = types.InlineKeyboardButton(text='-', callback_data='decrement')
    count = types.InlineKeyboardButton(text=str(current_amount), callback_data=str(current_amount))
    add_to_cart = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='to_cart')

    if plus_or_minus == 'increment':
         new_amount = int(current_amount) + 1
         count = types.InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))
    elif plus_or_minus == 'decrement':
        if int(current_amount) > 1:
            new_amount = int(current_amount) - 1
            count = types.InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))

    kb.add(minus, count, plus)
    kb.row(add_to_cart)
    kb.row(back)
    return kb

def cart_buttons():
    kb = types.InlineKeyboardMarkup(row_width=1)
    clear_cart = types.InlineKeyboardButton(text='Очистить корзину', callback_data='clear_cart')
    order = types.InlineKeyboardButton(text='Оформить заказ', callback_data='order')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    kb.add(clear_cart, order, back)
    return kb

