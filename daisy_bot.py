#!/usr/bin/env python3
"""
DaisyAI Vortex Bot – Interactive setup (asks for token & chat ID on first run)
"""

import os
import json
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
    ConversationHandler,
)

CONFIG_FILE = "bot_config.json"

# ========== LOAD OR ASK FOR CREDENTIALS ==========
def load_or_setup_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    else:
        print("\n🔧 First-time setup – let's configure your bot.\n")
        token = input("👉 Enter your BotFather token: ").strip()
        chat_id = input("👉 Enter your Telegram chat ID (numerical): ").strip()
        if not token or not chat_id:
            raise ValueError("Both token and chat ID are required.")
        config = {"BOT_TOKEN": token, "CREATOR_CHAT_ID": chat_id}
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f)
        print("✅ Config saved to bot_config.json. You won't be asked again.\n")
        return config

config = load_or_setup_config()
BOT_TOKEN = config["BOT_TOKEN"]
CREATOR_CHAT_ID = str(config["CREATOR_CHAT_ID"])

# Conversation states
NAME, PROJECT, BUDGET = range(3)

# ========== YOUR BIO (same as before) ==========
BIO = """
🔥 **HNIC — Builder, Systems Thinker, Inventor, Entrepreneur**

A multidisciplinary builder with experience spanning:
• Manufacturing & heavy industry
• Aerospace & defense (F-22, Tomahawk)
• Automotive repair & performance
• R&D, product design & prototyping
• Software development & AI systems
• Business development & sales

**Daisy Ecosystem Founder:**
DaisyOS | DaisyAI | DaisyChain | DaisyMedia | DaisyMarkets | DaisyApps | DaisyGames | DaisyOracle | Daisy Global Racing

🏭 Industrial: Ford Tier 1, Defasco Steel, Rossborough, Moen R&D
✈️ Aerospace: F-22 Raptor, Tomahawk fuel systems
🚗 Automotive: Mobile repair, engine/transmission building, performance mods
💻 Tech: AI agent design, object detection, AR racing systems, GitHub projects

*“I don’t specialize in one thing – I connect systems others miss.”*
"""

SPECS = """
🌀 **Vortex X1 – 102mm Iris Throttle Body**

• 9 flat titanium blades – true iris mechanism
• Idle: 2mm near‑circular hole (no center nipple)
• WOT: Blades fully retract into housing wall – 102mm clear bore
• CNC machined aluminum housing, drive‑by‑wire actuator
• Compatible with LS1, LS2, LS3, LS4, LS5, LS6
• No airflow obstruction at full throttle
• Designed by Douglas Owens Jr. (OwenSonicInfinity)
"""

# ========== COMMAND HANDLERS ==========
async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("📄 My Experience", callback_data="experience")],
        [InlineKeyboardButton("🔧 Vortex X1 Specs", callback_data="specs")],
        [InlineKeyboardButton("🎤 Start Interview", callback_data="interview")],
        [InlineKeyboardButton("📞 Contact Douglas", callback_data="contact")],
    ]
    await update.message.reply_text(
        "🌼 *DaisyAI here – your Vortex X1 concierge.*\n\n"
        "I represent Douglas Owens Jr., the builder behind the Daisy ecosystem and the Vortex X1 iris throttle.\n\n"
        "What would you like to do?",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown",
    )

async def experience(update: Update, context):
    await update.message.reply_text(BIO, parse_mode="Markdown")

async def specs(update: Update, context):
    await update.message.reply_text(SPECS, parse_mode="Markdown")

async def contact(update: Update, context):
    await update.message.reply_text(
        "📧 *Email:* owensonicinfinity@gmail.com\n"
        "📱 *Phone:* 440-281-6270\n"
        "🌐 *GitHub / Portfolio:* owensonicinfinity.netlify.app\n\n"
        "Or just keep chatting – I'll forward your message to Douglas directly.",
        parse_mode="Markdown",
    )

# ========== INTERVIEW CONVERSATION ==========
async def interview_start(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "🎤 *Let’s start a quick interview.*\n\n"
        "Douglas uses this to understand who’s interested in the Vortex X1 or the Daisy ecosystem.\n\n"
        "What’s your *full name*?",
        parse_mode="Markdown",
    )
    return NAME

async def interview_name(update: Update, context):
    context.user_data["name"] = update.message.text
    await update.message.reply_text(
        f"Thanks {update.message.text}. What *project* are you working on?\n"
        "(e.g., LS6 swap, custom fabrication, DaisyOS integration, etc.)",
        parse_mode="Markdown",
    )
    return PROJECT

async def interview_project(update: Update, context):
    context.user_data["project"] = update.message.text
    await update.message.reply_text(
        "Do you have a *budget or timeline*? (If not, just say 'not sure')",
        parse_mode="Markdown",
    )
    return BUDGET

async def interview_budget(update: Update, context):
    context.user_data["budget"] = update.message.text
    name = context.user_data["name"]
    project = context.user_data["project"]
    budget = context.user_data["budget"]

    # Forward to creator's Telegram
    interview_msg = (
        f"📋 *New Interview Lead*\n"
        f"Name: {name}\n"
        f"Project: {project}\n"
        f"Budget/Timeline: {budget}\n"
        f"From: @{update.effective_user.username or 'no username'}"
    )
    await context.bot.send_message(
        chat_id=CREATOR_CHAT_ID, text=interview_msg, parse_mode="Markdown"
    )

    await update.message.reply_text(
        "✅ *Thank you!* Douglas will review your info and reach out shortly.\n\n"
        "In the meantime, you can ask me about specs, experience, or use /help.",
        parse_mode="Markdown",
    )
    return ConversationHandler.END

async def cancel(update: Update, context):
    await update.message.reply_text("Interview cancelled. Type /start to begin again.")
    return ConversationHandler.END

# ========== BUTTON CALLBACK ==========
async def button_callback(update: Update, context):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "experience":
        await query.edit_message_text(BIO, parse_mode="Markdown")
    elif data == "specs":
        await query.edit_message_text(SPECS, parse_mode="Markdown")
    elif data == "contact":
        await query.edit_message_text(
            "📧 *Email:* owensonicinfinity@gmail.com\n"
            "📱 *Phone:* 440-281-6270\n"
            "🌐 *GitHub:* owensonicinfinity.netlify.app\n\n"
            "Douglas usually replies within 24 hours.",
            parse_mode="Markdown",
        )
    elif data == "interview":
        await query.edit_message_text(
            "🎤 *Interview started.*\n\nWhat’s your *full name*?",
            parse_mode="Markdown",
        )
        return NAME
    return ConversationHandler.END

# ========== ECHO FORWARDER ==========
async def forward_to_creator(update: Update, context):
    """Any non‑command message is forwarded to the creator."""
    if update.message.text and not update.message.text.startswith("/"):
        await context.bot.send_message(
            chat_id=CREATOR_CHAT_ID,
            text=f"💬 From @{update.effective_user.username or 'anonymous'}: {update.message.text}",
        )
        await update.message.reply_text("Message forwarded to Douglas. He'll reply soon.")

# ========== MAIN ==========
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("experience", experience))
    app.add_handler(CommandHandler("specs", specs))
    app.add_handler(CommandHandler("contact", contact))

    # Conversation for interview
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("interview", lambda u, c: interview_start(u, c)),
            CallbackQueryHandler(button_callback, pattern="^interview$"),
        ],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, interview_name)],
            PROJECT: [MessageHandler(filters.TEXT & ~filters.COMMAND, interview_project)],
            BUDGET: [MessageHandler(filters.TEXT & ~filters.COMMAND, interview_budget)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler)

    # Button callbacks (non‑interview)
    app.add_handler(CallbackQueryHandler(button_callback))

    # Forward any other text to creator
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_creator))

    print("🤖 DaisyAI Vortex bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
