from mubble import Dispatch, CallbackQuery, MessageCute, ParseMode
from mubble.rules import CallbackData

from hermid.keyboards import menu, currency

dp = Dispatch()


@dp.callback_query(CallbackData("currency"))
async def currency_handler(cq: CallbackQuery):
    text = "🏦 Тут ви можете переглянути курси світових валют та криптовалют"

    await cq.edit_text(
       text,
       parse_mode=ParseMode.HTML,
       reply_markup=currency
   )