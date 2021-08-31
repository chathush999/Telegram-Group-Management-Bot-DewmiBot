import requests
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
from DewmiBot import dispatcher
from DewmiBot.modules.disable import DisableAbleCommandHandler


@run_async
def covid(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text.split(" ", 1)
    if len(text) == 1:
        r = requests.get("https://corona.lmao.ninja/v2/all").json()
        reply_text = f"**🦠 Corona Virus Results 🦠**\n🌡 Confirmed: {r['cases']:,}\nCases Today: {r['todayCases']:,}\n⚰️  Deaths: {r['deaths']:,}\nDeaths Today: {r['todayDeaths']:,}\n♻️ Recovered: {r['recovered']:,}\n🩸 Active: {r['active']:,}\nCritical: {r['critical']:,}\nCases/Mil: {r['casesPerOneMillion']}\nDeaths/Mil: {r['deathsPerOneMillion']}"
        reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="Updates", url="t.me/sl_bot_zone")]],
            )
    else:
        variabla = text[1]
        r = requests.get(f"https://corona.lmao.ninja/v2/countries/{variabla}").json()
        reply_text = f"**🦠 Corona Virus Results{r['country']} 🦠**\n🌡 Confirmed: {r['cases']:,}\nCases Today: {r['todayCases']:,}\n⚰️  Deaths: {r['deaths']:,}\nDeaths Today: {r['todayDeaths']:,}\n♻️ Recovered: {r['recovered']:,}\n🩸 Active: {r['active']:,}\nCritical: {r['critical']:,}\nCases/Mil: {r['casesPerOneMillion']}\nDeaths/Mil: {r['deathsPerOneMillion']}"
        reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="Updates", url="t.me/sl_bot_zone")]],
            )
        message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)
    


COVID_HANDLER = DisableAbleCommandHandler(["covid", "corona"], covid)
dispatcher.add_handler(COVID_HANDLER)
