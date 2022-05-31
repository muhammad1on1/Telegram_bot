import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, BotCommand, InputMediaPhoto

ADMIN = 'id'
TOKEN = 'token'

def start_command(update, context):
    global buttons
    buttons = [
        [InlineKeyboardButton(text='Send photo', callback_data='send_photo'),
         InlineKeyboardButton(text='Send Documend', callback_data='send_doc'),
         InlineKeyboardButton(text='Change Photo', callback_data='change_photo')],
        [InlineKeyboardButton(text='Send Media Group', callback_data='send_group')]
    ]
    update.message.reply_photo(
        # photo=open('photo/salom_bot.jpg', 'rb'),
        photo='https://picsum.photos/400/200',
        caption='Assalomu alaykum',
        reply_markup=InlineKeyboardMarkup(buttons)
    )


def message_handler(update, context):
    if context.user_data.get('matn'):
        words = context.user_data['matn']
    else:
        words = []
    words.append(update.message.text)
    context.user_data['matn'] = words
    print(f"{update.message.from_user.username}: {words}")



def inline_message(update, context):
    query = update.callback_query
    global buttons
    if query.data == 'send_doc':
         query.message.reply_document(
             document=open('Face_recognition.py'),
             caption='Telegram bot',
             reply_markup=InlineKeyboardMarkup(buttons)
         )

    elif query.data == 'send_photo':
        query.message.reply_photo(
            photo=f'https://picsum.photos/id/{random.randint(1,100)}/400/200',
            caption='Random Photo',
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    elif query.data == 'change_photo':
        query.message.edit_media(media=InputMediaPhoto(media=f'https://picsum.photos/id/{random.randint(1,100)}/400/200'))
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))

    elif query.data == 'send_group':
        query.message.reply_media_group(
            media=[
                InputMediaPhoto(media=open('photo/tarvuz.jpg', 'rb')),
                InputMediaPhoto(media=f'https://picsum.photos/id/{random.randint(1, 100)}/400/200'),
                InputMediaPhoto(media=f'https://picsum.photos/id/{random.randint(1, 100)}/400/200')
            ]
        )
def photo_handler(update, context):
    file = update.message.photo[-1].file_id
    obj = context.bot.get_file(file)
    obj.download('photo/user_foto.jpg')

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start_command))
dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
dispatcher.add_handler(CallbackQueryHandler(inline_message))
updater.start_polling()
updater.idle()
