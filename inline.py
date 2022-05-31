from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, ChatAction,  BotCommand, InlineKeyboardMarkup, InlineKeyboardButton

ADMIN = 'id'
TOKEN = 'token'

def start_command(update, context):
    # print(update.message.from_user.id)
    buttons = [
        [InlineKeyboardButton(text='Dasturlash', callback_data='dasturlash')],
        [InlineKeyboardButton(text='SMM', callback_data='smm')],
    ]

    update.message.reply_text(text=f"<i>Xush kelibsiz!</i> <b>{update.message.from_user.first_name}</b> \n<i>Bo'limni tanlang:</i> ",
                              parse_mode='HTML',
                              reply_markup=InlineKeyboardMarkup(buttons))



def info_command(update, context):
    # print(update.message.from_user.id)
    update.message.reply_text(text='Bu bot Face identifikater qiladi.')


def show_menu(update, context):
    buttons = [
        # [KeyboardButton(text='Kontakni yuborish', request_contact=True),
        #  KeyboardButton(text='Lokatsiyani yuborish', request_location=True)],
        [KeyboardButton(text='IT'), KeyboardButton(text='Moliya')],
    ]
    update.message.reply_text(
        text='Sohalar:',
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True))

def inline_message(update, context):
    query = update.callback_query
    if query.data == 'dasturlash':
        buttons = [
            [InlineKeyboardButton(text='Backend', callback_data='bd')],
            [InlineKeyboardButton(text='Frontend', callback_data='fd')],
        ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))

    if query.data == 'bd':
        buttons = [
            [InlineKeyboardButton(text='Python', callback_data='py')],
            [InlineKeyboardButton(text='java script', callback_data='js')],
            [InlineKeyboardButton(text='PHP', callback_data='php')]
        ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))

    if query.data == 'py':
        query.message.reply_text(text='python haqida malumot')


def message_handler(update, context):
    message = update.message.text
    update.message.reply_text(text=f'Sizning xabaringiz "{message}"')
    # update.message.reply_chat_action(action=ChatAction.TYPING)
    if message == 'IT':
        buttons = [
            [KeyboardButton(text='Backend'), KeyboardButton(text='Frontend')],
        ]
        update.message.reply_text(
            text='Fullstack: ',
            reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
        )
    if message == 'Backend':
        buttons = [
            [KeyboardButton(text='Python'), KeyboardButton(text='Java')],
            [KeyboardButton(text='PHP'), KeyboardButton(text='JavaScript')],
        ]
        update.message.reply_text(
            text='Dasturlash tillari:',
            reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
        )
    if message == 'Python':
        update.message.reply_text('Python hozirda eng yaxshi dasturlash tillaridan')




def contact_handler(update, context):
    phone_number = update.message.contact.phone_number
    print(phone_number)
    # update.message.reply_text(text=f'Sizning no\'meringiz "{phone_number}"')
    context.bot.send_message(chat_id=ADMIN, text=f'Yangi foydalanuvchi raqami: {phone_number}')


def location_handler(update, context):
     location = update.message.location
     print(location)
     # update.message.reply_location(latitude=location.latitude, longitude=location.longitude)
     context.bot.send_location(chat_id=ADMIN, latitude=location.latitude, longitude=location.longitude )
#

def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('info', info_command))
    dispatcher.add_handler(CommandHandler('menu', show_menu))
    dispatcher.add_handler(CallbackQueryHandler(inline_message))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(MessageHandler(Filters.location, location_handler))


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()