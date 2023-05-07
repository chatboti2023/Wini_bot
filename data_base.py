# libs
from aiogram import *
from aiogram.types import *
import sqlite3 as SQL

#vars
chanels_to_bot = []

# data base
data_base = SQL.connect("piar.db")

cursor = data_base.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS `users` (
                    `ID` STRING,
                    `Проверка_подписки` STRING,
                    `Дата_начала_подписки` STRING,
                    `Ваш_реферальный_код` STRING,
                    `Пригласительный_реферальный_код` STRING,
                    `Баланс` STRING,
                    `Город` STRING)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS `chanels` (
                    `ID_канала` STRING,
                    `ID_владельца` STRING)
""")

async def get_db():
    global id_list, check_list, subscribe_list, users_ref_list, ref_list, money_list, home_list, reg_list, chanels_list, id_chanels_list

    with data_base:
        # get element
        cursor = data_base.cursor()

        cursor.execute(f"SELECT ID FROM users")
        
        get_to_list = cursor.fetchall()
        id_list = get_to_list

        cursor.close()

        # to_list
        size_list = len(get_to_list)

        for i in range(size_list):
            id_list[i] = id_list[i][0]

        # get element
        cursor = data_base.cursor()

        cursor.execute(f"SELECT Проверка_подписки FROM users")
        
        get_to_list = cursor.fetchall()
        check_list = get_to_list

        cursor.close()

        # to_list
        size_list = len(get_to_list)

        for i in range(size_list):
            check_list[i] = check_list[i][0]

        # get element
        cursor = data_base.cursor()

        cursor.execute(f"SELECT Дата_начала_подписки FROM users")
        
        get_to_list = cursor.fetchall()
        subscribe_list = get_to_list

        cursor.close()

        # to_list
        size_list = len(get_to_list)

        for i in range(size_list):
            subscribe_list[i] = subscribe_list[i][0]

        # get element
        cursor = data_base.cursor()

        cursor.execute(f"SELECT Ваш_реферальный_код FROM users")
        
        get_to_list = cursor.fetchall()
        users_ref_list = get_to_list

        cursor.close()

        # to_list
        size_list = len(get_to_list)

        for i in range(size_list):
            users_ref_list[i] = users_ref_list[i][0]

        # get element
        cursor = data_base.cursor()

        cursor.execute(f"SELECT Пригласительный_реферальный_код FROM users")
        
        get_to_list = cursor.fetchall()
        ref_list = get_to_list

        cursor.close()

        # to_list
        size_list = len(get_to_list)

        for i in range(size_list):
            ref_list[i] = ref_list[i][0]

        # get element
        cursor = data_base.cursor()

        cursor.execute(f"SELECT Баланс FROM users")
        
        get_to_list = cursor.fetchall()
        money_list = get_to_list

        cursor.close()

        # to_list
        size_list = len(get_to_list)

        for i in range(size_list):
            money_list[i] = money_list[i][0]

        # get element
        cursor = data_base.cursor()

        cursor.execute(f"SELECT Город FROM users")
        
        get_to_list = cursor.fetchall()
        home_list = get_to_list

        cursor.close()

        # to_list
        size_list = len(get_to_list)

        for i in range(size_list):
            home_list[i] = home_list[i][0]

        # get element
        cursor = data_base.cursor()

        cursor.execute(f"SELECT ID_канала FROM chanels")
        
        get_to_list = cursor.fetchall()
        chanels_list = get_to_list

        cursor.close()

        # to_list
        size_list = len(get_to_list)

        for i in range(size_list):
            chanels_list[i] = chanels_list[i][0]

        # get element
        cursor = data_base.cursor()

        cursor.execute(f"SELECT ID_владельца FROM chanels")
        
        get_to_list = cursor.fetchall()
        id_chanels_list = get_to_list

        cursor.close()

        # to_list
        size_list = len(get_to_list)

        for i in range(size_list):
            id_chanels_list[i] = id_chanels_list[i][0]


async def started(message, referal_code):
    with data_base:
        cursor = data_base.cursor()

        cursor.execute(f"INSERT INTO `users` VALUES ({message.from_user.id}, 'нет', 'нет', {referal_code}, 'нет', 0, 'нет')")
        data_base.commit()


async def update(UPDATE, SET, WHERE, update_data, where_data):
    with data_base:
        cursor = data_base.cursor()

        cursor.execute(f"UPDATE {UPDATE} SET {SET} = '{update_data}' WHERE {WHERE} = {where_data}")

        data_base.commit()

        
async def add_chanel(chanel_url, admin_id):
    with data_base:
        cursor = data_base.cursor()

        cursor.execute(f"INSERT INTO `chanels` VALUES ('{chanel_url}', '{admin_id}')")
        data_base.commit()


async def get_chanel(id):
    global chanels_to_bot

    with data_base:
        cursor = data_base.cursor()

        cursor.execute(f"SELECT ID_канала FROM chanels WHERE ID_владельца = {id}")
        chanels_to_bot = cursor.fetchall()

        data_base.commit()
