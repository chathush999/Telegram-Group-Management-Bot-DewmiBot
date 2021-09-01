import asyncio
import os
import subprocess
import time

import psutil
from pyrogram import filters

from DewmiBot import (bot_start_time, DEV_USERS, pbot)


# Stats Module


async def bot_sys_stats():
    stats = f"""
This is called F-SUB so   
if you want to message in this group
you have to TG -Channel
and press the Unmute me button.
මෙකට කියන්නේ F-SUB කියලා ඉතින් ඔයාට මේ Group එකේ message  කරන්න ඔන්නම්  TG -Channel වෙලා Unmute me button එක ඔබන්න වෙනවා.
Info - @slbotzone
Call me private
"""
   
