from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton, InputMediaPhoto, ChatAction
import face_recognition
import numpy as np
import jsonn
ADMIN = 'id'
TOKEN = 'token'


def start_command(update, context):
    # print(update.message.from_user.id)
    update.message.reply_photo(
        photo=open('rasm/astrum.jpg', 'rb'),
        caption=f'Assalamu alaykum {update.message.from_user.first_name}\nMa\'lumot olish uchun /menu komandasini bosing. Yo\'nalishni tanlang va rasm yuboring!!!\n')
    context.bot.send_message(chat_id=ADMIN, text=f"@{update.message.from_user.username} foydalanuvchisi botga /start berdi!")

def info_command(update, context):
    update.message.reply_photo(
        photo=open('rasm/astrum1.jpg', 'rb'),
        caption=f'Assalamu alaykum {update.message.from_user.first_name}\nSiz bu botda "Astrum IT academiya" sida o\'qiydigan o\'quvchilar haqida ma\'lumot olishingiz mumkin. Ma\'lumot olish uchun\t  /start komandasini bosing,\t  /menu ga kiring. Yo\'nalishni tanlang va rasm yuboring!!!\n')



def show_menu(update, context):
    buttons = [
        [KeyboardButton(text='Data science')],
        [KeyboardButton(text='Software Engineer'), KeyboardButton(text='Full stack')]]
    update.message.reply_text(
        text='Menu',
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
    )

def message_handler(update, context):
    message = update.message
    message.reply_text(text="Siz rasm yuborishingiz mumkin:")


def photo_handler(update, context):
    context.bot.send_message(chat_id=ADMIN, text=f"@{update.message.from_user.username} foydalanuvchisi botni tekshirib ko'rdi!!!")
    file = update.message.photo[-1].file_id
    obj = context.bot.get_file(file)
    obj.download("rasm/bot.jpg")

    with open("student.json") as json_file:
        data = json.load(json_file)

    face_encodings = [np.asarray(i['encode']) for i in data]
    face_names = [f"Astrum o'quvchisi: \nYo'nalishi:   {i['dir']}\nToliq ismi:   {i['name']}" for i in data]

    bot_to_pic = face_recognition.load_image_file("rasm/bot.jpg")
    bot_encode_pic = face_recognition.face_encodings(bot_to_pic)[0]
    w = face_recognition.api.compare_faces(face_encodings, bot_encode_pic, tolerance=0.5)

    if True not in w:  update.message.reply_text(f"Bu o'quvchi bazada topilmadi.")
    for idx, i in enumerate(w):
        if i:
            update.message.reply_text(f"{face_names[idx]}")


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('info', info_command))
    dispatcher.add_handler(CommandHandler('menu', show_menu))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()