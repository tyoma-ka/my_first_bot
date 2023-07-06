from aiogram import Bot, Dispatcher, executor, types
import settings

bot = Bot(settings.API_KEY)
db = Dispatcher(bot)


@db.message_handler(content_types=['photo'])
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Hello')
    # await message.answer('Hello')
    await message.reply('Hello')
    # await message.answer_photo('photo')


@db.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site', url='https://apple.com'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)


@db.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)


@db.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Website'))
    await message.answer('Hello', reply_markup=markup)

executor.start_polling(db)