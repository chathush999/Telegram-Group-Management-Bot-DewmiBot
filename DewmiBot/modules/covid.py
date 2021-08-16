import requests
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

from DewmiBot import dispatcher
from DewmiBot.modules.disable import DisableAbleCommandHandler


@run_async
def covid(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text.split(" ", 1)
    if len(text) == 1:
        r = requests.get("https://corona.lmao.ninja/v2/all").json()
        reply_text = f"**Global Totals** 🦠\n😓Cases: {r['cases']:,}\n😓Cases Today: {r['todayCases']:,}\n😓Deaths: {r['deaths']:,}\n😓Deaths Today: {r['todayDeaths']:,}\nRecovered: {r['recovered']:,}\n😓Active: {r['active']:,}\n😓Critical: {r['critical']:,}\n😓Cases/Mil: {r['casesPerOneMillion']}\n😓Deaths/Mil: {r['deathsPerOneMillion']}"
    else:
        variabla = text[1]
        r = requests.get(f"https://corona.lmao.ninja/v2/countries/{variabla}").json()
        reply_text = f"**Cases for {r['country']} 🦠**\nCases: {r['cases']:,}\n😓Cases Today: {r['todayCases']:,}\n😓Deaths: {r['deaths']:,}\n😓Deaths Today: {r['todayDeaths']:,}\nRecovered: {r['recovered']:,}\n😓Active: {r['active']:,}\n😓Critical: {r['critical']:,}\n😓Cases/Mil: {r['casesPerOneMillion']}\n😓Deaths/Mil: {r['deathsPerOneMillion']}"
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


COVID_HANDLER = DisableAbleCommandHandler(["covid", "corona"], covid)
dispatcher.add_handler(COVID_HANDLER)
