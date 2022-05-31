from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton, ChatAction

ADMIN = 'id'
TOKEN = 'token'

def start_command(update, context):
    # print(update.message.from_user.id)
    update.message.reply_text(text='Botda /start va /menu comandalari ishlaydi')
    # context.bot.send_message(chat_id='x', text='Assalamu alykum')


def show_menu(update, context):
    buttons = [
        [KeyboardButton(text='Kontakni yuborish', request_contact=True),
         KeyboardButton(text='Lokatsiyani yuborish', request_location=True)],
        [KeyboardButton(text='Menu3'), KeyboardButton(text='Menu4')],
    ]
    update.message.reply_text(
        text='Menu',
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
    )

def message_handler(update, context):
    message = update.message.text
    update.message.reply_text(text=f'Sizning xabaringiz "{message}"')
    # update.message.reply_chat_action(action=ChatAction.TYPING)


def contact_handler(update, context):
    phone_number = update.message.contact.phone_number
    # update.message.reply_text(text=f'Sizning no\'meringiz "{phone_number}"')
    context.bot.send_message(chat_id=ADMIN, text=f'Yangi foydalanuvchi raqami: {phone_number}')


def location_handler(update, context):
     location = update.message.location
     print(location)
     # update.message.reply_location(latitude=location.latitude, longitude=location.longitude)
     context.bot.send_location(chat_id=ADMIN, latitude=location.latitude, longitude=location.longitude )


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('menu', show_menu))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(MessageHandler(Filters.location, location_handler))


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()