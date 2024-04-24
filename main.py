import telebot
import schedule
import time
from datetime import datetime
import sqlite3
import random

con = sqlite3.connect("Проект Школа.sqlite")
cur = con.cursor()
res666 = cur.execute(f"""SELECT id FROM V 
    WHERE name = ("МГУ")""").fetchall()
print(res666)
con.close()
con2 = sqlite3.connect("Проект Школа.sqlite")
cur2 = con2.cursor()
res2 = cur2.execute(f"""SELECT ol_id FROM O_V 
        WHERE v_id = {res666[0][0]}""").fetchall()
con2.close()
print(res2)
o00 = []
for i in res2:

    con3 = sqlite3.connect("Проект Школа.sqlite")
    cur3 = con3.cursor()
    res3 = cur3.execute(f"""SELECT name FROM O 
                WHERE id = {i[0]}""").fetchall()
    con3.close()
    print(res3)
    o00.append(res3[0][0])
    print(res3)


con = sqlite3.connect("Проект Школа.sqlite")
cur = con.cursor()
res222 = cur.execute(f"""SELECT id FROM V 
    WHERE name = ("ВШЭ")""").fetchall()
print(res222)
con.close()
con2 = sqlite3.connect("Проект Школа.sqlite")
cur2 = con2.cursor()
res2 = cur2.execute(f"""SELECT ol_id FROM O_V 
        WHERE v_id = {res222[0][0]}""").fetchall()
con2.close()
print(res2)
o33 = []
for i in res2:

    con3 = sqlite3.connect("Проект Школа.sqlite")
    cur3 = con3.cursor()
    res3 = cur3.execute(f"""SELECT name FROM O 
                WHERE id = {i[0]}""").fetchall()
    con3.close()
    print(res3)
    o33.append(res3[0][0])
    print(res3)
print(o33)



def get_parameter(text):
    try:
        return ' '.join(text.split()[1:]) if len(text.split()) > 1 else False
    except:
        return False
con = sqlite3.connect("Проект Школа.sqlite")
cur = con.cursor()
resols = cur.execute(f"""SELECT name, link FROM O""").fetchall()
con.close()
bot = telebot.TeleBot('6938592889:AAG3lk3iwpOG1ag-wHvkyU5wEH0sfLbclSo')
con = sqlite3.connect("Проект Школа.sqlite")
cur = con.cursor()
res = cur.execute(f"""SELECT name, dates FROM O 
    """).fetchall()
olimpiad_dates = {}
con.close()
months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
months1 = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
for i in res:
    olimpiad_dates[(i[0])] = eval(i[1])
jobs = {}

o = []
con = sqlite3.connect("Проект Школа.sqlite")
cur = con.cursor()
res = cur.execute(f"""SELECT name, link FROM O""").fetchall()

jlp = dict()
for i in res:
    jlp[i[0][-30:]] = i[0]
con.close()
print(jlp)

@bot.message_handler(commands=['fil'])
def help_message1(message):
    print(message.from_user.id)
    if message.from_user.id == 1038099964 or message.from_user.id == 1571685995:
        r = random.randint(0, 100)
        if r <= 30:
            bot.send_message(message.chat.id, 'Экспериментальный центр напоминает вам, что вы - ГЕЙ! И идёте в жопу с этим говном')
        else:
            bot.send_message(message.chat.id, 'Экспериментальный центр напоминает вам, что вы - торт')
    else:
        bot.send_message(message.chat.id, 'Ты не Фил')


def job(chat_id, olimpiad, key):
    con = sqlite3.connect("Проект Школа.sqlite")
    cur = con.cursor()
    res = cur.execute(f"""SELECT link FROM O 
            WHERE name = ("{(olimpiad)}")""").fetchall()
    print(res)
    con.close()
    j = olimpiad_dates[(olimpiad)][key]
    date, time = j.split(' ')
    year, month, day = date.split('-')
    string = str(day) + ' ' + months[int(month) - 1] + ' ' + str(year) + ' года' + ' в ' + time
    olimpiad = '\)'.join(('\('.join(olimpiad.split('('))).split(')'))
    key = '\)'.join(('\('.join(key.split('('))).split(')'))
    bot.send_message(chat_id, "Скоро [" + olimpiad + '](' + res[0][0] + ') ' + key + ', а если быть точнее ' + string, parse_mode='MarkdownV2', disable_web_page_preview=True)
    return schedule.CancelJob

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Список доступных команд:\n/start - Начать общение с ботом\n/help - Получить помощь по использованию бота\n/remind - Запланировать напоминание олимпиады\n/univ_to [название ВУЗа] - Список олимпиад дающих бонусы в ВУЗ\n/olimp [название олимпиады] - Описание олимпиады\n/olimp_list - Список олимпиад\n/univ_list - Список ВУЗов')

@bot.message_handler(commands=['start'])
def help_message(message):
    bot.send_message(message.chat.id, 'Список доступных команд:\n/start - Начать общение с ботом\n/help - Получить помощь по использованию бота\n/remind - Запланировать напоминание олимпиады\n/univ_to [название ВУЗа] - Список олимпиад дающих бонусы в ВУЗ\n/olimp [название олимпиады] - Описание олимпиады\n/olimp_list - Список олимпиад\n/univ_list - Список ВУЗов')

@bot.message_handler(commands=['remind'])
def reuqest_message(message):
    bot.send_message(message.chat.id, 'Введи название олимпиады, про которую хотите видеть напоминания')
    @bot.message_handler(content_types=['text'])
    def send_text(message):
        try:
            users_olimpiad = message.text
            print(olimpiad_dates[users_olimpiad])
            for key, value in olimpiad_dates[users_olimpiad].items():

                user_date_time = datetime.strptime(value, '%Y-%m-%d %H:%M')
                delta = user_date_time - datetime.now()
                jobs[message.chat.id] = schedule.every(delta.total_seconds() - 86400).seconds.do(job, message.chat.id, users_olimpiad, str(key))
                bot.send_message(message.chat.id, 'Напоминания запланированы!')
        
        except KeyError:
            bot.send_message(message.chat.id, 'Такой олимпиады нет')
        except ValueError:
            bot.send_message(message.chat.id, 'Напоминания запланированы!')
            

@bot.message_handler(commands=["univ_to"])
def olimp1(message):
    try:
        if type(message) == str:
            param = message
        else:
            param = get_parameter(message.text)
        if param == 'МГУ':
            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            bl = []
            for i in o00[:-24]:
                print({str(i[0][-30:])})
                button = telebot.types.InlineKeyboardButton(str(i), callback_data=f"test_{str(i[-30:])}")
                bl.append(button)
            markup.add(*bl)
            button = telebot.types.InlineKeyboardButton('=>', callback_data=f"next pagem")
            markup.add(button)
            bot.send_message(message.chat.id, 
                        text='<pre>Олимпиады:                                                                                                                                                    ㅤ &#x200D;</pre>', 
                        parse_mode='HTML', reply_markup=markup)
        elif param == 'ВШЭ':
            markup = telebot.types.InlineKeyboardMarkup(row_width=1)
            bl = []
            for i in o33[:-24]:
                print({str(i[0][-30:])})
                button = telebot.types.InlineKeyboardButton(str(i), callback_data=f"test_{str(i[-30:])}")
                bl.append(button)
            markup.add(*bl)
            button = telebot.types.InlineKeyboardButton('=>', callback_data=f"next pagev")
            markup.add(button)
            bot.send_message(message.chat.id, 
                        text='<pre>Олимпиады:                                                                                                                                                    ㅤ &#x200D;</pre>', 
                        parse_mode='HTML', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Такого ВУЗа нет в списке')
        #final = '\n'.join(o)
        #markup = telebot.types.InlineKeyboardMarkup()
        #for i in o:
        #    print({str(i[-30:])})
        #    button = telebot.types.InlineKeyboardButton(str(i), callback_data=f"test_{str(i[-30:])}")
        #    markup.add(button)
        #bot.send_message(message.chat.id, "Олимпиады:", reply_markup=markup)
    except Exception as e:
        bot.send_message(message.chat.id, 'Такого ВУЗа нет в списке')

@bot.message_handler(commands=["olimp"])
def olimp2(message, param=None):
    print('---------------')
    try:
        
        if param is None:
            param = get_parameter(message.text)

        con = sqlite3.connect("Проект Школа.sqlite")
        cur = con.cursor()
        res = cur.execute(f"""SELECT id FROM O 
            WHERE name = ("{param}")""").fetchall()
        print(res)
        con.close()
        con2 = sqlite3.connect("Проект Школа.sqlite")
        cur2 = con2.cursor()
        res2 = cur2.execute(f"""SELECT v_id, requirements, BVI, points FROM O_V 
                WHERE ol_id = {res[0][0]}""").fetchall()
        con2.close()
        o = []
        bon = 'Бонусы: \n'
        for i in res2:

            con3 = sqlite3.connect("Проект Школа.sqlite")
            cur3 = con3.cursor()
            res3 = cur3.execute(f"""SELECT name, link FROM V 
                        WHERE id = {i[0]}""").fetchall()
            con3.close()
            print(res2)
            o.append((res3[0][0], i[1], i[2], i[3]))
            print(i[2])
            bv = ''
            if i[2] == 'w':
                bv = 'победителям'
            elif i[2] == 'wp':
                bv = 'победителям и победителям'
            else:
                bv = 'не даёт'

            bl = ''
            print(i[3])
            if i[3] == 'w':
                bl = 'победителям'
            elif i[3] == 'wp':
                bl = 'победителям и победителям'
            else:
                bl = 'не даёт'

            bon +='  '+ res3[0][0] + ':' + '\n' + '     требования по баллам ЕГЭ: ' + i[1]+ '\n' + '     БВИ: ' + bv+ '\n' + '     100 баллов: ' + bl + '\n'+ '\n'
            print(res3)
        print(o)


        con = sqlite3.connect("Проект Школа.sqlite")
        cur = con.cursor()
        res = cur.execute(f"""SELECT * FROM O 
            WHERE name = ("{param}")""").fetchall()
        print(res)
        con.close()
        print(olimpiad_dates[str(res[0][1])])
        fi = 'Название: ' + str(res[0][1]) + '\n'+ '\n'
        fi += 'Предмет: ' + str(res[0][2]) + '\n'
        print(str(res[0][4]))
        if not str(res[0][4]) == '-':
            fi += 'Специфика: ' + str(res[0][4]) + '\n'
        fi += 'Ссылка: ' + str(res[0][6]) + '\n'+ '\n'
        fi += bon + '\n'
        fi += 'Даты: ' + '\n'
        for key, value in olimpiad_dates[str(res[0][1])].items():
            if not value == '-':
                month = value
                fi += '   ' + key + ': ' + months1[int(month) - 1] + '\n'

        #if len(fi) > 4095:
        #    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        #    for x in range(0, len(m), 4095):
        #        bot.reply_to(message, text=m[x:x+4095])
        #    else:
        #        bot.reply_to(message, text=m)
        bot.send_message(message.chat.id, fi)
    except Exception as e:
        bot.send_message(message.chat.id, 'Такой олимпиады нет в списке')

@bot.message_handler(commands=["olimp_list"])
def olimp3(message):
    print(message.from_user.id)

    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    bl = []
    for i in resols[:-24]:
        button = telebot.types.InlineKeyboardButton(str(i[0]), callback_data=f"test_{str(i[0][-30:])}")
        bl.append(button)
    markup.add(*bl)
    button = telebot.types.InlineKeyboardButton('=>', callback_data=f"next page")
    markup.add(button)
    bot.send_message(message.chat.id, 
                 text='<pre>Олимпиады:                                                                                                                                                    ㅤ &#x200D;</pre>', 
                 parse_mode='HTML', reply_markup=markup)




@bot.message_handler(commands=["univ_list"])
def olimp4(message):
    con = sqlite3.connect("Проект Школа.sqlite")
    cur = con.cursor()
    res = cur.execute(f"""SELECT name, link FROM V""").fetchall()
    print(res)
    con.close()
    fi = 'Список ВУЗов:\n' + '\n'.join(list(map(lambda x: '[' + x[0] + '](' + x[1] + ')', res)))
    bot.send_message(message.chat.id, fi, parse_mode='MarkdownV2', disable_web_page_preview=True)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data.startswith("test_"):
        bot.answer_callback_query(call.id)
        print(jlp[call.data.split("_")[1]])
        olimp2(call.message, jlp[call.data.split("_")[1]])
    if call.data == "next page":
        keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
        bl = []
        for i in resols[-24:]:
            print({str(i[0][-30:])})
            button = telebot.types.InlineKeyboardButton(str(i[0]), callback_data=f"test_{str(i[0][-30:])}")
            bl.append(button)
        keyboard.add(*bl)
        button = telebot.types.InlineKeyboardButton('<=', callback_data=f"perv page")
        keyboard.add(button)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard)
    
    if call.data == "perv page":
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        bl = []
        for i in resols[:-24]:
            print({str(i[0][-30:])})
            button = telebot.types.InlineKeyboardButton(str(i[0]), callback_data=f"test_{str(i[0][-30:])}")
            bl.append(button)
        markup.add(*bl)
        button = telebot.types.InlineKeyboardButton('=>', callback_data=f"next page")
        markup.add(button)
    

        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
    


    if call.data == "next pagem":
        keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
        bl = []
        for i in o00[-24:]:
            print({str(i[-30:])})
            button = telebot.types.InlineKeyboardButton(str(i), callback_data=f"test_{str(i[-30:])}")
            bl.append(button)
        keyboard.add(*bl)
        button = telebot.types.InlineKeyboardButton('<=', callback_data=f"perv pagem")
        keyboard.add(button)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard)
    
    if call.data == "perv pagem":
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        bl = []
        for i in o00[:-24]:
            print({str(i[-30:])})
            button = telebot.types.InlineKeyboardButton(str(i), callback_data=f"test_{str(i[-30:])}")
            bl.append(button)
        markup.add(*bl)
        button = telebot.types.InlineKeyboardButton('=>', callback_data=f"next pagem")
        markup.add(button)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)


    if call.data == "next pagev":
        keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
        bl = []
        for i in o33[-24:]:
            print({str(i[-30:])})
            button = telebot.types.InlineKeyboardButton(str(i), callback_data=f"test_{str(i[-30:])}")
            bl.append(button)
        keyboard.add(*bl)
        button = telebot.types.InlineKeyboardButton('<=', callback_data=f"perv pagev")
        keyboard.add(button)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=keyboard)
    
    if call.data == "perv pagev":
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        bl = []
        for i in o33[:-24]:
            print({str(i[-30:])})
            button = telebot.types.InlineKeyboardButton(str(i), callback_data=f"test_{str(i[-30:])}")
            bl.append(button)
        markup.add(*bl)
        button = telebot.types.InlineKeyboardButton('=>', callback_data=f"next pagev")
        markup.add(button)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
def run_pending():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    import threading
    threading.Thread(target=run_pending).start()
    bot.polling(none_stop=True)

#------------------------------------------#
