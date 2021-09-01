import asyncio
import os
import subprocess
import time

import psutil
from pyrogram import filters



# Stats Module


async def bot_sys_stats():
    bot_uptime = int(time.time() - bot_start_time)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    stats = f"""
This is called F-SUB so   
if you want to message in this group
you have to TG -Channel
and press the Unmute me button.
මෙකට කියන්නේ F-SUB කියලා ඉතින් ඔයාට මේ Group එකේ message  කරන්න ඔන්නම්  TG -Channel වෙලා Unmute me button එක ඔබන්න වෙනවා.
Info - @slbotzone
Call me private
"""
   
