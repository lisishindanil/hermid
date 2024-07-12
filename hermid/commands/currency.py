from mubble import Dispatch, CallbackQuery, ParseMode
from mubble.rules import CallbackData
from mubble.client import AiohttpClient

from hermid import keyboards
from hermid.utils.currencies import Currency, Cryptocurrency

from hermid.config import EXCHANGE_API, COIN_API

dp = Dispatch()
currency = Currency(EXCHANGE_API)
crypto_currency = Cryptocurrency(COIN_API)

@dp.callback_query(CallbackData("currency"))
async def currency_handler(cq: CallbackQuery):
    await cq.edit_text(
        "<b>🏦 Тут ви можете переглянути курси світових валют та криптовалют</b>\n\n"
        "💡 Оберіть тип валюти нижче",
        reply_markup=keyboards.currency,
        parse_mode=ParseMode.HTML
    )
    await cq.answer()


@dp.callback_query(CallbackData("currency_rates"))
async def currency_rates_handler(cq: CallbackQuery):
    vaults = {"USD": "🇺🇸", "EUR": "🇪🇺", "GBP": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "CAD": "🇨🇦", "PLN": "🇵🇱"}
    result = await currency.get_currency("UAH")

    currencies_text = ""
    for i, c in vaults.items():
        currency_value = result[i]
        currencies_text += (
            f"{c} <b>{currency_value:.4f}</b> {i} | <b>{(1 / currency_value):.3f}</b> UAH\n"
        )

    await cq.edit_text(
        "<b>🌍 Актуальний курс світових валют</b>\n\n"
        f"<blockquote>{currencies_text}</blockquote>\n\n"
        "💡 Використовуйте меню нижче",
        parse_mode=ParseMode.HTML,
        reply_markup=keyboards.back_to_menu,
    )
    await cq.answer()


@dp.callback_query(CallbackData("crypto_currency_rates"))
async def crypto_currency_rates_handler(cq: CallbackQuery):
    result = await crypto_currency.get_currency("BTC")

    await cq.edit_text(
        str(result),
        reply_markup=keyboards.back_to_menu
    )
    await cq.answer()