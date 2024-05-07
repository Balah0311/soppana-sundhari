from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, ContextTypes

from AsuX import rani


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    msg = update.effective_message
    akboss = []
    akboss.append(
        [
            InlineKeyboardButton(
                text="𝐀ᴅᴅ 𝐌ᴇ",
                url=f"http://t.me/{context.bot.username}?startgroup=true"),
            InlineKeyboardButton(
                text="𝐍ᴇᴛᴡᴏʀᴋ",
                url=f"https://t.me/team_hypers_networks"),
            
        ]
    )
    await msg.reply_text(
        f"╭──────⌁᳀⌁╾─────╮\n ‎ ‎ ‎ ‎ [𝐓ᴇᴀᴍ 𝐇ʏᴘᴇʀ 𝐍ᴇᴛᴡᴏʀᴋ](https://t.me/Team_Hypers_Networks)\n╰─────╼⌁᳀⌁╾─────╯</b>\n\n<b>𝐔ɴᴅᴇʀ 𝐇ʏᴘᴇʀ 𝐂ᴏɴᴛʀᴏʟ {context.bot.first_name}</b>\n\n<b>𝐀ɴʏ 𝐈ssᴜ 𝐓ᴏ 𝐂ᴏɴᴛᴀᴄᴛ 𝐓O 𝐇ʏᴘᴇʀ 𝐍ᴇᴛᴡᴏʀᴋ - [𝐓ᴇᴀᴍ 𝐇ʏᴘᴇʀ 𝐍ᴇᴛᴡᴏʀᴋ](https://t.me/Team_Hypers_Networks) </b>\n\n<b>",
        reply_markup=InlineKeyboardMarkup(akboss),
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    msg = update.effective_message
    akboss = []
    akboss.append(
        [
            InlineKeyboardButton(
                text="𝐀ᴅᴅ 𝐌ᴇ",
                url=f"http://t.me/{context.bot.username}?startgroup=true"),
            InlineKeyboardButton(
                text="𝐍ᴇᴛᴡᴏʀᴋ",
                url=f"https://t.me/team_hypers_networks"),
        ]
    )
    await msg.reply_text(
        f"╭──────⌁᳀⌁╾─────╮\n ‎ ‎ ‎ ‎ [𝐓ᴇᴀᴍ 𝐇ʏᴘᴇʀ 𝐍ᴇᴛᴡᴏʀᴋ](https://t.me/Team_Hypers_Networks)\n╰─────╼⌁᳀⌁╾─────╯</b>\n\n<b>𝐔ɴᴅᴇʀ 𝐇ʏᴘᴇʀ 𝐂ᴏɴᴛʀᴏʟ {context.bot.first_name}</b>\n\n<b>𝐀ɴʏ 𝐈ssᴜ 𝐓ᴏ 𝐂ᴏɴᴛᴀᴄᴛ 𝐓O 𝐇ʏᴘᴇʀ 𝐍ᴇᴛᴡᴏʀᴋ - [𝐓ᴇᴀᴍ 𝐇ʏᴘᴇʀ 𝐍ᴇᴛᴡᴏʀᴋ](https://t.me/Team_Hypers_Networks) </b>\n\n<b>",",
        reply_markup=InlineKeyboardMarkup(akboss),
    )


START = CommandHandler(["chatbot", "start"], start, block=True)
HELP = CommandHandler(["chelp", "help"], help, block=True)

rani.add_handler(START)
rani.add_handler(HELP)
