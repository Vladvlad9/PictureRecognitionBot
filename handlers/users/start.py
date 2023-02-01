from aiogram import types

from loader import dp, bot

import easyocr


async def text_description(file_path):
    reader = easyocr.Reader(["ru", "en", "be"])
    result = reader.readtext(file_path, detail=0, paragraph=True)
    return result


@dp.message_handler(content_types=["photo"])
async def process_message(message: types.Message):
    photo = await bot.get_file(message.photo[len(message.photo) - 1].file_id)
    await bot.download_file(photo.file_path, destination='new_img.jpg', timeout=12, chunk_size=1215000)
    await message.answer(text="Ожидайте, я обрабатываю картинку")
    get_photo = await text_description(file_path="new_img.jpg")
    if get_photo:
        await message.answer(text=get_photo)
        print(get_photo)
    else:
        await message.answer(text="Не удалось распознать картинку!")


@dp.message_handler(commands=["start"])
async def registration_start(message: types.Message):
    await message.answer(text="Добро пожаловать в бот по распознаванию изображений\n\n"
                              "Что бы воспользоваться моим функционалом просто отправь мне картинку")
