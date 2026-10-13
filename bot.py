import asyncio
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,ReplyKeyboardMarkup,KeyboardButton

bot = Bot(token="8767538554:AAHSL4D_8JIESKIN22b_9gXmFzQIa8PRh1A")

dp = Dispatcher()

reply_keyboards = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Mercedes-Benz S-Class"),
        
            KeyboardButton(text="Mercedes-AMG GT 63 S")
        ],[
            KeyboardButton(text="Mercedes-CLS AMG 63 banan"),
        
            KeyboardButton(text="Mercedes-AMG G 63")
        ],[
            KeyboardButton(text="Mercedes-AMG C 63"),

            KeyboardButton(text="Mercedes W211")
        ]
       
    ],
     resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Xush kelibsiz !!!",
    reply_markup= reply_keyboards
    )
@dp.message(Command("help"))
async def help(message:Message):
    await message.answer("kechirasz yordam beraolmayman !!!")

@dp.message(F.text == "Mercedes-Benz S-Class")
async def S_Class(message: Message):
    await message.answer_photo(photo=
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqo995ptppxN" \
"UAmfGISyHRsfT_OE0lobwYrMt9JGuG_VcR7dDlmx81gSs&s=10")

@dp.message(F.text == "Mercedes-AMG GT 63 S")
async def S_Class(message: Message):
    await message.answer_photo(photo=
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQG9YOmXD6yRQGg" \
    "P2FKHS3b7BMTREWaWYGyYqToCyvZu8mxfdai_SY17x8&s=10")

@dp.message(F.text == "Mercedes-CLS AMG 63 banan")
async def S_Class(message: Message):
    await message.answer_photo(photo=
    "https://encrypted-tbn0.gstatic.com/images?q=" \
    "tbn:ANd9GcTK62jz4L3SHeCrM5ctv_W2ksCTjoCxya5L7PIqqfrga7jkMvP5P-A9TuS5&s=10")

@dp.message(F.text == "Mercedes-AMG G 63")
async def S_Class(message: Message):
    await message.answer_photo(photo=
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9G" \
    "cQSP1jNuwxGFCRwYH5fT-BO4ceGVbKxgDeLR0LdmaDpxwHd7BEJe7VjVOs&s=10")

@dp.message(F.text == "Mercedes-AMG C 63")
async def S_Class(message: Message):
    await message.answer_photo(photo=
    "https://media.istockphoto.com/id/1415376026/photo/mercedes-benz-c63-s-driving.jpg?s" \
    "=2048x2048&w=is&k=20&c=BwzpjAtWa3cGMAtQJBKhOotCJiuU5qDH6bg_VngmCAM=")

@dp.message(F.text == "Mercedes W211")
async def S_Class(message: Message):
    await message.answer_photo(photo=
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:" \
    "ANd9GcRYlGj4B7Bg4SNd1vVNAJMJGkIMsNTQ9Cd713wkxhdI41byqTBa9EIT9P4&s=10")

@dp.message()
async def javob_yozish(message: Message):
    await message.answer("Qabul qilindi!")
    await bot.send_message(
        chat_id=6268083159,
        text=f"Yangi xabar: {message.text}"
        )

async def main():
    await dp.start_polling(bot)

asyncio.run(main())