from mubble import Dispatch, Message, CallbackQuery
from mubble.rules import StartCommand, CallbackData
from mubble.tools import ParseMode

from hermid.keyboards import menu

dp = Dispatch()
text = (
    "<b>👋 Вітаємо в нашому фінансовому помічнику! 📊💰</b>\n\n"
    "Наш бот допоможе вам:"
    "<blockquote>🏦 Перевіряти курси валют та криптовалют в режимі реального часу\n\n"
    "🌐 Отримувати свіжі новини світової економіки\n\n"
    "🤖 Використовувати можливості штучного інтелекту для аналізу фінансових даних\n\n"
    "🗺️ Знаходити найближчі банкомати на карті\n\n"
    "📈 Вести облік доходів та витрат та аналізувати їх</blockquote>\n\n"
    "Ми тут, щоб допомогти вам управляти вашими фінансами легко та зручно! 🚀"
)


@dp.message(StartCommand())
async def start_handler(msg: Message):

    await msg.answer(
        text,
        parse_mode=ParseMode.HTML,
        reply_markup=menu
    )

@dp.callback_query(CallbackData("menu"))
async def menu_handler(cq: CallbackQuery):
    await cq.delete()

    await cq.ctx_api.send_message(
        chat_id=cq.chat_id,
        text=text,
        parse_mode=ParseMode.HTML,
        reply_markup=menu
    )