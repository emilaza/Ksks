from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import time
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
KANAL_ID = os.getenv("KANAL_ID")

IT = Client(
	"İtiraf Bot",
	api_id=API_ID,
	api_hash=API_HASH,
	bot_token=BOT_TOKEN
	)

CHL = -1001786824396

PM = 5128216420

@IT.on_message(filters.command("start") & filters.private)
async def start(client: IT, message: Message):
	await message.reply_text(f"<b> {message.from_user.mention} Hoş Geldin🥰,Ben @mutsuz_panda tərəıindən hazırlanan bir itiraf botu’yum.\nİtiraflarınız @mutsuz_panda kanalında paylaşılacak🤓.\n\nSende bir itiraf etmək istiyorsan  komutlar;\nAnonim İtiraf: /ano mesaj\nAçık İtiraf: /itiraf mesaj</b>")

@IT.on_message(filters.command("ano") & filters.private)
async def ano(client: IT, message: Message):
	text = " ".join(message.command[1:])
	if text == "":
		await message.reply_text("Lütfen bir itiraf yazarak tekrar deneyin📣.")
	else:
		await IT.send_message(chat_id=CHL, text=f"Gönderen: ANONİM\nİtiraf: {text}")
		time.sleep(0.5)
		await IT.send_message(chat_id=PM, text=f"Gönderen: {message.from_user.mention}\nİtiraf: {text}")
		time.sleep(0.5)
		await message.reply_text("İtirafınız sahibime gönderildiği onaylandıktan sonra @mutsuz_panda kanalında paylaşılacaktır🥰.")

@IT.on_message(filters.command("itiraf") & filters.private)
async def itf(client: IT, message: Message):
	t = " ".join(message.command[1:])
	if t == "":
		await message.reply_text("Lütfen bir itiraf yazarak tekrar deneyin😶.")
	else:
		await IT.send_message(chat_id=CHL, text=f"Gönderen: {message.from_user.mention}\nİtiraf: {t}")
		time.sleep(0.5)
		await message.reply_text("İtirafınız sahibime gönderildiği onaylandıktan sonra @mutsuz_panda kanalında paylaşılacaktır🥰.")

IT.run()
