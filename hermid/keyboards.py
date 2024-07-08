from mubble import InlineKeyboard, InlineButton


menu = (
    InlineKeyboard()
    .add(InlineButton("🏦 Курси валют", callback_data="currency"))
    .add(InlineButton("🌐 Новини", callback_data="news"))
    .add(InlineButton("🤖 AI помічник", callback_data="ai_helper"))
    .row()
    .add(InlineButton("🗺️ Мапа банкоматів", callback_data="atm_map"))
    .add(InlineButton("📈 Облік", callback_data="accounting"))
    .row()
    .add(InlineButton("⚙️ Налаштування", callback_data="settings"))
).get_markup()

back_to_menu = (
    InlineKeyboard().add(InlineButton("↩️ Назад", callback_data="menu"))
).get_markup()

currency = (
    InlineKeyboard()
    .add(InlineButton("Світові валюти", callback_data="currency_rates"))
    .add(InlineButton("Крипто валюти", callback_data="crypto_currency_rates"))
    .row()
    .add(InlineButton("↩️ Назад", callback_data="menu"))
).get_markup()