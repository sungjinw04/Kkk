from Sung import logger 
from pyrogram import idle
import importlib
from Sung import Bot
from Sung.modules import ALL_MODULES

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("Sung.modules." + module_name)

if name == "main":
  Bot.start()
  logger.info("Bot is up and running...")
  idle()
  Bot.stop()
  logger.info("Bot has stopped")

    
