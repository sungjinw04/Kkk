import logging 
from pyrogram import Client, idle

from motor.motor_asyncio import AsynclOMotorClient
from Sung.config.py import OWNER_ID, API_ID, API_HASH, MONGO_DB, SUPPORT_GROUP, SUPPORT_CHANNEL, BOT_TOKEN, BOT_USERNAME, JOINLOGS, LEAVELOGS

class Config:
  OWNER_ID = OWNER_ID
  API_ID = API_ID
  API_HASH = API_HASH
  MONGO_DB = MONGO_DB
  SUPPORT_GROUP = SUPPORT_GROUP
  SUPPORT_CHANNEL = SUPPORT_CHANNEL
  BOT_TOKEN = BOT_TOKEN
  BOT_USERNAME = BOT_USERNAME
  LEAVELOGS = LEAVELOGS
  JOINLOGS = JOINLOGS

logging.basicConfig(
  format='%(asctime)s-%(name)s-%
  (levelname)s-%(message)s',
  level=logging.INFO) 
logger = logging.getlogger(name)




Bot= Client(
  "testing bot"
  api_id=Config.API_ID,
  api_hash=Config.API_HASH,
  bot_token=Config.BOT_TOKEN
  )
  
  
