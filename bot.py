from aiogram import Bot,Dispatcher,executor,types
from googletrans import Translator
from api import taom_qaytar
import logging


logging.basicConfig(level=logging.INFO)
bot=Bot(token="6111209465:AAFyTvnZlrUA_iGBmf545eUMpR2qLhC04fc")
dp=Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(xabar:types.Message):
    await xabar.reply(f"salom {xabar.chat.full_name}.\nTaom hohlisanmi?\n /taom ni bos!!!")

@dp.message_handler(commands='taom')
async def xabar(message:types.Message):
    meals=taom_qaytar()
    nomi=meals['strMeal']
    hududi=meals['strArea']
    categoriya=meals['strCategory']
    rasmi=meals['strMealThumb']
    videosi=meals['strYoutube']
    text=f"🍛🍛🥗🥗 {nomi}\n{hududi}\n{categoriya} taomi \nTayyorlanish usuli ⤵️⤵️⤵️"
    tarjimon=Translator()
    textuz=tarjimon.translate(text,dest='uz').text
    await message.answer_photo(photo=rasmi,caption=textuz)
    await message.answer(videosi)
if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)
