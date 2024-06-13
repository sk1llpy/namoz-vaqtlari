import math
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.regions import REGIONS
from functions.API.users import get_user

def button(current_page: int, user_id):
    next_page = current_page + 1

    regions = REGIONS

    current_index = 0
    max_length_width = 3
    max_length_height = 4

    max_length = max_length_width * max_length_height

    pages = len(regions) / max_length
    pages = math.ceil(pages)

    buttons = []

    y = 0
    for x in range(pages):
        buttons.append([])

        y += 1
        for l in range(int(max_length * y - max_length), min(max_length * y, len(regions))):
            buttons[y - 1].append(regions[l])

    regions_btn_lst = []

    if current_page == 0:
        regions_btn_lst.append(
            [
                InlineKeyboardButton(
                    text = '📍 Mening shaharim', 
                    callback_data = get_user(user_id=user_id).json()['region'] if get_user(user_id=user_id).json()['region'] else 'Toshkent'
                )
            ]
        )

        if current_page < len(buttons):
            page_buttons = buttons[current_page]
            page_btn_row = []
            for reg in page_buttons:
                page_btn_row.append(InlineKeyboardButton(
                    text=reg,
                    callback_data=reg
                ))
                if len(page_btn_row) == max_length_width:
                    regions_btn_lst.append(page_btn_row)
                    page_btn_row = []

            # Append the last row if it's not already appended
            if page_btn_row:
                regions_btn_lst.append(page_btn_row)

        regions_btn_lst.append(
            [
                InlineKeyboardButton("⬅️", callback_data=f'back_{current_page - 1}'),
                InlineKeyboardButton(f"{current_page + 1}/{pages-1}", callback_data='page'),
                InlineKeyboardButton("➡️", callback_data=f'next_{current_page + 1}')
            ]
        )
    else:
        if current_page < len(buttons):
            page_buttons = buttons[current_page + 1]
            page_btn_row = []
            for reg in page_buttons:
                page_btn_row.append(InlineKeyboardButton(
                    text=reg,
                    callback_data=reg
                ))
                if len(page_btn_row) == max_length_width:
                    regions_btn_lst.append(page_btn_row)
                    page_btn_row = []

            # Append the last row if it's not already appended
            if page_btn_row:
                regions_btn_lst.append(page_btn_row)

        regions_btn_lst.append(
            [
                InlineKeyboardButton("⬅️", callback_data=f'back_{current_page - 1}'),
                InlineKeyboardButton(f"{current_page + 1}/{pages - 1}", callback_data='page'),
                InlineKeyboardButton("➡️", callback_data=f'next_{current_page + 1}')
            ]
        )

    regions_btn_lst.append([InlineKeyboardButton("⬅️ Asosiy menu", callback_data='backto_menu')])
    regions_btn = InlineKeyboardMarkup(inline_keyboard=regions_btn_lst)

    return regions_btn


def button_week(current_page: int, user_id: int):
    next_page = current_page + 1

    regions = REGIONS

    current_index = 0
    max_length_width = 3
    max_length_height = 4

    max_length = max_length_width * max_length_height

    pages = len(regions) / max_length
    pages = math.ceil(pages)

    buttons = []

    y = 0
    for x in range(pages):
        buttons.append([])

        y += 1
        for l in range(int(max_length * y - max_length), min(max_length * y, len(regions))):
            buttons[y - 1].append(regions[l])

    regions_btn_lst = []

    if current_page == 0:
        regions_btn_lst.append(
            [
                InlineKeyboardButton(
                    text = '📍 Mening shaharim', 
                    callback_data = f"{get_user(user_id=user_id).json()['region']}_week" if get_user(user_id=user_id).json()['region'] else 'Toshkent_week'
                )
            ]
        )

        if current_page < len(buttons):
            page_buttons = buttons[current_page]
            page_btn_row = []
            for reg in page_buttons:
                page_btn_row.append(InlineKeyboardButton(
                    text=reg,
                    callback_data=f'{reg}_week'
                ))
                if len(page_btn_row) == max_length_width:
                    regions_btn_lst.append(page_btn_row)
                    page_btn_row = []

            # Append the last row if it's not already appended
            if page_btn_row:
                regions_btn_lst.append(page_btn_row)

        regions_btn_lst.append(
            [
                InlineKeyboardButton("⬅️", callback_data=f'backweek_{current_page - 1}'),
                InlineKeyboardButton(f"{current_page + 1}/{pages-1}", callback_data='page'),
                InlineKeyboardButton("➡️", callback_data=f'nextweek_{current_page + 1}')
            ]
        )
    else:
        if current_page < len(buttons):
            page_buttons = buttons[current_page + 1]
            page_btn_row = []
            for reg in page_buttons:
                page_btn_row.append(InlineKeyboardButton(
                    text=reg,
                    callback_data=f'{reg}_week'
                ))
                if len(page_btn_row) == max_length_width:
                    regions_btn_lst.append(page_btn_row)
                    page_btn_row = []

            # Append the last row if it's not already appended
            if page_btn_row:
                regions_btn_lst.append(page_btn_row)

        regions_btn_lst.append(
            [
                InlineKeyboardButton("⬅️", callback_data=f'backweek_{current_page - 1}'),
                InlineKeyboardButton(f"{current_page + 1}/{pages - 1}", callback_data='page'),
                InlineKeyboardButton("➡️", callback_data=f'nextweek_{current_page + 1}')
            ]
        )

    regions_btn_lst.append([InlineKeyboardButton("⬅️ Asosiy menu", callback_data='backto_menu')])
    regions_btn = InlineKeyboardMarkup(inline_keyboard=regions_btn_lst)

    return regions_btn


def button_change(current_page: int):
    next_page = current_page + 1

    regions = REGIONS

    current_index = 0
    max_length_width = 3
    max_length_height = 4

    max_length = max_length_width * max_length_height

    pages = len(regions) / max_length
    pages = math.ceil(pages)

    buttons = []

    y = 0
    for x in range(pages):
        buttons.append([])

        y += 1
        for l in range(int(max_length * y - max_length), min(max_length * y, len(regions))):
            buttons[y - 1].append(regions[l])

    regions_btn_lst = []

    if current_page == 0:
        if current_page < len(buttons):
            page_buttons = buttons[current_page]
            page_btn_row = []
            for reg in page_buttons:
                page_btn_row.append(InlineKeyboardButton(
                    text=reg,
                    callback_data=reg
                ))
                if len(page_btn_row) == max_length_width:
                    regions_btn_lst.append(page_btn_row)
                    page_btn_row = []

            # Append the last row if it's not already appended
            if page_btn_row:
                regions_btn_lst.append(page_btn_row)

        regions_btn_lst.append(
            [
                InlineKeyboardButton("⬅️", callback_data=f'back_{current_page - 1}'),
                InlineKeyboardButton(f"{current_page + 1}/{pages-1}", callback_data='page'),
                InlineKeyboardButton("➡️", callback_data=f'next_{current_page + 1}')
            ]
        )
    else:
        if current_page < len(buttons):
            page_buttons = buttons[current_page + 1]
            page_btn_row = []
            for reg in page_buttons:
                page_btn_row.append(InlineKeyboardButton(
                    text=reg,
                    callback_data=reg
                ))
                if len(page_btn_row) == max_length_width:
                    regions_btn_lst.append(page_btn_row)
                    page_btn_row = []

            # Append the last row if it's not already appended
            if page_btn_row:
                regions_btn_lst.append(page_btn_row)

        regions_btn_lst.append(
            [
                InlineKeyboardButton("⬅️", callback_data=f'back_{current_page - 1}'),
                InlineKeyboardButton(f"{current_page + 1}/{pages - 1}", callback_data='page'),
                InlineKeyboardButton("➡️", callback_data=f'next_{current_page + 1}')
            ]
        )

    regions_btn_lst.append([InlineKeyboardButton("⬅️ Asosiy menu", callback_data='backto_menu')])
    regions_btn = InlineKeyboardMarkup(inline_keyboard=regions_btn_lst)

    return regions_btn

