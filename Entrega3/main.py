from sre_parse import SPECIAL_CHARS
import telebot
from telebot import types


lower_case = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'á', 'b', 'c', 'd', 'e', 'é', 'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l',
              'm', 'n', 'ñ', 'o', 'ó', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'v', 'w', 'x', 'y', 'z']
upper_case = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'Á', 'B', 'C', 'D', 'E', 'É', 'F', 'G', 'H', 'I', 'Í', 'J', 'K', 'L',
              'M', 'N', 'Ñ', 'O', 'Ó', 'P', 'Q', 'R', 'S', 'T', 'U', 'Ú', 'V', 'W', 'X', 'Y', 'Z']

SPECIAL_CHARS = ['!', '@', '#', '$', '%', '^', '&', '*',
                 '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ':', ';', '"', '\'', '<', '>', '?', '/', '.', ',', '~', '`', ' ']

print(len(lower_case))
print(len(SPECIAL_CHARS))

des = 1

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# !,	",	#,	$,	%,	&,	',	(,	),	*,	+,	,,	-,	.,	/  :	;	<	=	>	?


def ceasar_cipher(text, des):
    cifrado = ""
    words = text.split(" ")
    for word in words:
        for caracter in word:
            # print(caracter)
            if caracter in lower_case:
                cifrado += lower_case[(lower_case.index(caracter) + des) %
                                      len(lower_case)]

                # print(cifrado)
            if caracter in upper_case:
                cifrado += upper_case[(upper_case.index(caracter) + des) %
                                      len(upper_case)]

            if caracter in SPECIAL_CHARS:
                cifrado += SPECIAL_CHARS[(SPECIAL_CHARS.index(caracter) + des) %
                                         len(SPECIAL_CHARS)]

        cifrado += " "

    print("La palabra encriptada es: ", cifrado)
    return cifrado


def ceasar_decipher(text):

    dcifrado = ""
    messages = ""
    words = text.split(" ")
    for des in range(1, len(lower_case)+1):
        dcifrado = ""
        for word in words:
            for caracter in word:
                # print(caracter)
                if caracter in lower_case:
                    dcifrado += lower_case[(lower_case.index(caracter) - des) %
                                           len(lower_case)]

                    # print(cifrado)
                if caracter in upper_case:
                    dcifrado += upper_case[(upper_case.index(caracter) - des) %
                                           len(upper_case)]
                if caracter in SPECIAL_CHARS:
                    dcifrado += SPECIAL_CHARS[(SPECIAL_CHARS.index(caracter) - des) %
                                              len(SPECIAL_CHARS)]

                dcifrado += " "

        messages += f"Opcion {des} : {dcifrado}"
        messages += "\n"
        #print(f"Opcion {des} : " , dcifrado)
    print(messages)
    return messages


API_TOKEN = '5300335502:AAFAm_W81EIpeECW1ds6PAyj4hEIpU0tCrE'

bot = telebot.TeleBot(API_TOKEN)

user_dict = {}


class User:
    def __init__(self, msg):
        self.msg = msg
        self.dis = None


@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.reply_to(
        message, """Hello there, I'm JemBot a bot that will encrypt all the message that you want""")


@bot.message_handler(commands=['help'])
def send_help(message):
    msg_ = bot.reply_to(message, """\nAvailable Commands :-
    /brightspace - To get the Brightspace URL
    /encrypt - To encrypt the message that you want
    /decypher - To decode the message that you want""")


@bot.message_handler(commands=['encrypt'])
def process_encrypt_step(message):
    msg = bot.reply_to(
        message, """Hello there, send me the message that you want to encrypt""")
    bot.register_next_step_handler(msg, process_shift_step)


def process_shift_step(message):
    try:
        chat_id = message.chat.id
        text = message.text
        user = User(text)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'Enter the shift')
        bot.register_next_step_handler(msg, process_Fencrypt_step)
    except Exception as e:
        bot.reply_to(
            message, "Sorry, it looks like there was an error. Please try again.")


def process_Fencrypt_step(message):
    try:
        chat_id = message.chat.id
        shift = message.text
        if not shift.isdigit():
            msg = bot.reply_to(message, 'shift should be a number.')
            bot.register_next_step_handler(msg, process_Fencrypt_step)
            return
        user = user_dict[chat_id]
        user.dis = int(shift)

        bot.send_message(chat_id, 'Nice to meet you,  ' +
                         'your encrypted message is ' + ceasar_cipher(user.msg, user.dis))

    except Exception as e:
        print(e)
        bot.reply_to(
            message, 'Sorry, it looks like there was an error. Please try again.')


@bot.message_handler(commands=['decypher'])
def process_encrypt_step(message):
    msg = bot.reply_to(
        message, """Hello there, send me the message that you want to decypher""")
    bot.register_next_step_handler(msg, process_decypher_step)


def process_decypher_step(message):
    try:
        chat_id = message.chat.id
        text = message.text
        user = User(text)
        user_dict[chat_id] = user
        bot.send_message(chat_id, 'Nice to meet you,  ' +
                         'your decoded message is ' + ceasar_decipher(user.msg))
    except Exception as e:
        bot.reply_to(
            message, "Sorry, it looks like there was an error. Please try again.")


bot.enable_save_next_step_handlers(delay=2)


bot.load_next_step_handlers()

bot.infinity_polling()