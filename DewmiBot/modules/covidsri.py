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
        r = requests.get("https://corona.lmao.ninja/v2/sri lanka").json()
        reply_text = f"**🇱🇰 Local Covid 19 Stats  🇱🇰**🩺\n📊 Total Confirmed Cases: {r['cases']:,}\n😷  New Cases Today : {r['todayCases']:,}\n💥 Deaths: {r['deaths']:,}\n💣  New Deaths today : {r['todayDeaths']:,}\n📟  Recovered & Discharged: {r['recovered']:,}\n🔖 Active Cases: {r['active']:,}\n🏥 Individuals currently under investigations in hospitals: {r['critical']:,}\nCases/Mil: {r['casesPerOneMillion']}\nDeaths/Mil: {r['deathsPerOneMillion']}"
        
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


COVID_HANDLER = DisableAbleCommandHandler(["covid", "corona"], covid)
dispatcher.add_handler(COVID_HANDLER)
