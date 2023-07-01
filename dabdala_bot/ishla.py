import logging
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍹Ichimliklar"),
            KeyboardButton(text="🥙Lavashlar"),
        ],
        [
            KeyboardButton(text="🍕Pitsalar"),
            KeyboardButton(text="🍔Burgerlar"),
        ],
        [
            KeyboardButton(text="🍰Shirinliklar"),
            KeyboardButton(text="📍Manzillar"),
            KeyboardButton(text="☎️Telefon_raqamlar")
        ],
    ],
    resize_keyboard=True
)

Manzillar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Manzil"),
        ],
        [
            KeyboardButton(text="🔙Orqaga")
        ]
    ],
    resize_keyboard=True
)



Telefon_raqamlar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="contact"),
        ],
        [
            KeyboardButton(text="🔙Orqaga")
        ],
    ],
    resize_keyboard=True
)


ichimliklar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍷Pepsi"),
            KeyboardButton(text="🍸Sprite"),
            KeyboardButton(text="🍹Fanta"),
        ],
        [
            KeyboardButton(text="🔙Orqaga")
        ],
    ],
    resize_keyboard=True
)



@dp.message_handler(commands=['start', 'menu'])
async def send_welcome(message: types.Message):
    await message.reply("Assalamu aleykum", reply_markup=bosh_menu)


@dp.message_handler(text="📍Manzillar")
async def send_welcome(message: types.Message):
    await message.reply("📍Manzillar", reply_markup=Manzillar_menu)

@dp.message_handler(text="Manzil")
async def send_welcome(message: types.Message):
    await message.answer_location(41.36614857876635, 69.27753210173728)


@dp.message_handler(text="☎️Telefon_raqamlar")
async def send_welcome(message: types.Message):
    await message.reply("☎️Telefon_raqamlar", reply_markup=Telefon_raqamlar_menu)

@dp.message_handler(text="contact")
async def send_welcome(message: types.Message):
    await message.answer_contact("+998 90 335 82 42", "ravshanovich_pm")



@dp.message_handler(text="🍹Ichimliklar")
async def send_welcome(message: types.Message):
    await message.reply("🍹Ichimliklar", reply_markup=ichimliklar_menu)

@dp.message_handler(text="🍸Sprite")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://catherineasquithgallery.com/uploads/posts/2021-03/1614585015_90-p-sprait-na-belom-fone-103.png",
                               caption="""
0.5L = 6.500 so'm
                               """)

@dp.message_handler(text="🍹Fanta")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://www.mercadadelivery.ru/wp-content/uploads/2020/08/fanta.jpg",
                               caption="""
0.5L = 7.000 so'm
                               """)

@dp.message_handler(text="🍷Pepsi")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://kartinkin.net/uploads/posts/2022-05/1653606372_26-kartinkin-net-p-pepsi-kola-kartinki-28.png",
                               caption="""
0.5L = 6.500 so'm
                               """)
    

shirinliklar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍥Medovik"),
            KeyboardButton(text="🥮Praga"),
            KeyboardButton(text="🥧Napaleon"),
            KeyboardButton(text="🍡Ekler"),
        ],
        [
            KeyboardButton(text="🔙Orqaga"),
        ],
    ],
    resize_keyboard=True
)
@dp.message_handler(text="🍰Shirinliklar")
async def send_welcome(message: types.Message):
    await message.reply("🍰Shirinliklar", reply_markup=shirinliklar_menu)

@dp.message_handler(text="🍥Medovik")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://main-cdn.sbermegamarket.ru/hlr-system/767/049/998/410/11/100030449787b0.jpg",
                               caption="""
1-kusok = 15.000 so'm
                               """)
    

@dp.message_handler(text="🥮Praga")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://mykaleidoscope.ru/uploads/posts/2021-09/1632280101_36-mykaleidoscope-ru-p-pirozhnoe-praga-krasivo-foto-42.jpg",
                               caption="""
1-kusok = 16.000 so'm
                               """)

@dp.message_handler(text="🥧Napaleon")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://mykaleidoscope.ru/x/uploads/posts/2022-10/1666282740_34-mykaleidoscope-ru-p-napoleon-klassicheskii-vkontakte-38.png",
                               caption="""
1-kusok = 17.000 so'm
                               """)

@dp.message_handler(text="🍡Ekler")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://image.shutterstock.com/shutterstock/photos/1305602695/display_1500/stock-photo-group-homemade-eclair-on-white-background-1305602695.jpg",
                               caption="""
1-dona = 7.000 so'm
                               """)



pitsalar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Go'shtli"),
            KeyboardButton(text="Pepperoni"),
            KeyboardButton(text="Margarita"),
            KeyboardButton(text="Tovuqli"),
        ],
        [
            KeyboardButton(text="🔙Orqaga"),
        ],
    ],
    resize_keyboard=True
)

@dp.message_handler(text="🍕Pitsalar")
async def send_welcome(message: types.Message):
    await message.reply("🍕Pitsalar", reply_markup=pitsalar_menu)

@dp.message_handler(text="Go'shtli")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://sun9-61.userapi.com/c841135/v841135830/15d25/OiTVdFOuPFU.jpg",
                               caption="""
50-sm = 55.000 so'm
                               """)

@dp.message_handler(text="Pepperoni")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://beerloga67.ru/img/food/2023_02_08_13_16_13_IKCSVMxwCN820Hvdz6WnWekQM8NmiTUJ.jpg",
                               caption="""
50-sm = 66.000 so'm
                               """)

@dp.message_handler(text="Margarita")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://adonius.club/uploads/posts/2022-01/1643138234_44-adonius-club-p-pitstsa-na-belom-fone-50.jpg",
                               caption="""
50-sm = 57.000 so'm
                               """)
    

@dp.message_handler(text="Tovuqli")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://tknugush.ru/upload/iblock/558/5589496b6a35926ab38c8fceb7b3b691.jpg",
                               caption="""
50-sm = 50.000 so'm
                               """)

@dp.message_handler(text="🔙Orqaga")
async def send_welcome(message: types.Message):
    await message.reply("Orqaga", reply_markup=bosh_menu)

burgerlar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Gamburger"),
            KeyboardButton(text="Chizburger"),
            KeyboardButton(text="Donar"),
            KeyboardButton(text="Dubl Chizburger"),
        ],
        [
            KeyboardButton(text="🔙Orqaga"),
        ],
    ],
    resize_keyboard=True
)

@dp.message_handler(text="🍔Burgerlar")
async def send_welcome(message: types.Message):
    await message.reply("🍔Burgerlar", reply_markup=burgerlar_menu)

@dp.message_handler(text="Gamburger")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://adonius.club/uploads/posts/2022-02/1644626199_10-adonius-club-p-foto-burgera-na-belom-fone-14.jpg",
                               caption="""
1-dona = 25.000 so'm
                               """)

@dp.message_handler(text="Chizburger")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://townsquare.media/site/390/files/2017/03/Cheeseburger.jpg?w=1200&amp;h=0&amp;zc=1&amp;s=0&amp;a=t&amp;q=89",
                               caption="""
1-dona = 26.000 so'm
                               """)

@dp.message_handler(text="Donar")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://s1.1zoom.ru/big3/185/Fast_food_Sandwich_Vegetables_White_background_569338_4235x3000.jpg",
                               caption="""
1-dona = 27.000 so'm
                               """)

@dp.message_handler(text="Dubl Chizburger")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://www.organicauthority.com/.image/t_share/MTU5MzMwNDkxNzA4Njc5Nzc2/burger-photo.jpg",
                               caption="""
1-dona = 30.000 so'm
                               """)


lavashlar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sirli"),
            KeyboardButton(text="Tovuqlii"),
            KeyboardButton(text="Go'shtlii"),
            KeyboardButton(text="Mix"),
        ],
        [
            KeyboardButton(text="🔙Orqaga"),
        ],
    ],
    resize_keyboard=True
)


@dp.message_handler(text="🥙Lavashlar")
async def send_welcome(message: types.Message):
    await message.reply("🥙Lavashlar", reply_markup=lavashlar_menu)

@dp.message_handler(text="Sirli")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://static.tildacdn.com/tild3438-3863-4336-b835-316134326635/_.jpg",
                               caption="""
1-dona = 25.000 so'm
                               """)
    

@dp.message_handler(text="Go'shtlii")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://phonoteka.org/uploads/posts/2022-09/1663880214_38-phonoteka-org-p-shaurma-belii-fon-vkontakte-53.jpg",
                               caption="""
1-dona = 26.000 so'm
                               """)

@dp.message_handler(text="Tovuqlii")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://w1.pngwing.com/pngs/230/617/png-transparent-chicken-shawarma-lavash-doner-kebab-vegetarian-cuisine-doner-king-pita-pork.png",
                               caption="""
1-dona = 27.000 so'm
                               """)

@dp.message_handler(text="Mix")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://phonoteka.org/uploads/posts/2022-09/1663880234_9-phonoteka-org-p-shaurma-belii-fon-vkontakte-12.png",
                               caption="""
1-dona = 30.000 so'm
                               """)
    
# @dp.message_handler(text="yakudza")
# async def send_welcome(message: types.Message):
#     await message.answer_video_note(video_note="https://telesco.pe/YAKUDZAForever/8529")

# @dp.message_handler(text="yakudzaa")
# async def send_welcome(message: types.Message):
#     await message.answer_voice(voice="https://t.me/YAKUDZAForever/8514")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)   
