from telegram import Update
from telegram.ext import CallbackContext, run_async

from DewmiBot import dispatcher
from DewmiBot.modules.disable import DisableAbleCommandHandler

EHI_STRINGS = "[click here more info](https://t.me/SL_bot_zone/509)"


@run_async
def ehi(update: Update, context: CallbackContext):
    update.effective_message.reply_text(EHI_STRINGS),
    parse_mode=ParseMode.MARKDOWN,
    disable_web_page_preview=True,

EHI_HANDLER = DisableAbleCommandHandler("vplay",vplay)
dispatcher.add_handler(EHI_HANDLER)
