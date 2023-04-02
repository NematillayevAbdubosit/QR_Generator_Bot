import qrcode, config, os, logging
from aiogram import Bot, Dispatcher, types, executor
from analytics import analytics

#logging
logging.basicConfig(level=logging.INFO)

prox_url = "http://proxy.server:3128"

# bot and dispatcher
bot = Bot(token=config.TOKEN, proxy=prox_url)
dp = Dispatcher(bot)


# start command
@dp.message_handler(commands=["start"])
@analytics
async def start(message: types.Message):
    await message.answer("Salom \nBu bot orqali siz qrcode yaratishingiz mumkin") 
    await message.answer("Matnni yoki havolanni kiriting 👇")


# main function
@dp.message_handler()
@analytics
async def qr_code(photo: types.Message):
    await photo.answer("Biroz kuting ...⏳")
    img = qrcode.make(photo.text)
    type(img)
    img.save("qr_code.png")
    await bot.send_photo(photo.chat.id, photo=open(f'qr_code.png', 'rb'))
    os.remove("qr_code.png")


# help command
@dp.message_handler(commands=["help"])
@analytics
async def help_msg(help_message: types.Message):
    await help_message.answer("Bu botni ishlatish uchun siz xohlagan so'zni qr-code ko'rinishida ko'rmoqchi "
                              "bo'lsangiz shunchaki matnni jo'nating.")


# run polling
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
