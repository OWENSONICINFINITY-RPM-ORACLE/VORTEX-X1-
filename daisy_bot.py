🤖 DaisyAI Vortex Bot – Complete Setup Guide

You want the DAISYAIVORTEXbot to have a persona (DaisyAI) and interview visitors who ask about your experience, the Vortex X1, or just want to talk. Below is everything BotFather will ask + the full bot code you can run in 10 minutes.

---

📋 Part 1: BotFather – What He’ll Ask You

Open Telegram → @BotFather → /newbot

BotFather Question Your Answer
Name (display name) DaisyAI Vortex X1
Username (must end in bot) DAISYAIVORTEXbot (already taken – you own it)
Would you like to set a description? (after creation) → /setdescription DaisyAI – Your AI assistant for Vortex X1. I know everything about the 9‑blade iris throttle, 102mm bore, and the creator’s journey. Ask me about experience, specs, or start an interview.
About text (/setabouttext) Builder, inventor, entrepreneur. DaisyOS ecosystem. Vortex X1 – world’s first retracting iris throttle body. DM me for interviews.
Profile picture (/setuserpic) Use the Vortex X1 logo or your photo
Commands (/setcommands) ```

start - Welcome & interview
experience - My background & journey
specs - Vortex X1 technical specs
contact - Get in touch with Douglas
help - What I can do ``` |

After that, copy the token (looks like 7234567890:AAH...). Keep it safe.

---

🧠 Part 2: The Bot Persona & Interview Logic

Here’s a ready‑to‑run Python script that:

· Greets visitors with your HNIC / builder intro
· Answers /experience with your full bio (from the text you sent)
· Runs an interview (asks name, project, budget/timeline) and forwards answers to your Telegram
· Responds to natural questions about the Vortex X1 (blades, bore, LS compatibility)

✅ What You Need

· Python 3.8+ installed on a computer or a free cloud host (Render, PythonAnywhere, or a Raspberry Pi)
· The bot token from BotFather
· Your personal Chat ID (to receive interview answers) – get it by sending a message to your bot, then visiting https://api.telegram.org/bot<TOKEN>/getUpdates

---

📦 The Bot Script

Create a new file called daisy_bot.py and paste the following:

```python
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ConversationHandler

# ========== CONFIGURATION ==========
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"          # Replace with token from BotFather
CREATOR_CHAT_ID = "YOUR_CHAT_ID_HERE"      # Your personal Telegram chat ID (as string)
# ====================================

# Conversation states
NAME, PROJECT, BUDGET = range(3)

# Your full bio (shortened for Telegram – use multiple messages)
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
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🌼 *DaisyAI here – your Vortex X1 concierge.*\n\n"
        "I represent Douglas Owens Jr., the builder behind the Daisy ecosystem and the Vortex X1 iris throttle.\n\n"
        "What would you like to do?",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def experience(update: Update, context):
    # Split long bio into multiple messages if needed
    await update.message.reply_text(BIO, parse_mode="Markdown")

async def specs(update: Update, context):
    await update.message.reply_text(SPECS, parse_mode="Markdown")

async def contact(update: Update, context):
    await update.message.reply_text(
        "📧 *Email:* owensonicinfinity@gmail.com\n"
        "📱 *Phone:* 440-281-6270\n"
        "🌐 *GitHub / Portfolio:* owensonicinfinity.netlify.app\n\n"
        "Or just keep chatting – I'll forward your message to Douglas directly."
    )

# ========== INTERVIEW CONVERSATION ==========
async def interview_start(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "🎤 *Let’s start a quick interview.*\n\n"
        "Douglas uses this to understand who’s interested in the Vortex X1 or the Daisy ecosystem.\n\n"
        "What’s your *full name*?",
        parse_mode="Markdown"
    )
    return NAME

async def interview_name(update: Update, context):
    context.user_data['name'] = update.message.text
    await update.message.reply_text(
        f"Thanks {update.message.text}. What *project* are you working on?\n"
        "(e.g., LS6 swap, custom fabrication, DaisyOS integration, etc.)",
        parse_mode="Markdown"
    )
    return PROJECT

async def interview_project(update: Update, context):
    context.user_data['project'] = update.message.text
    await update.message.reply_text(
        "Do you have a *budget or timeline*? (If not, just say 'not sure')",
        parse_mode="Markdown"
    )
    return BUDGET

async def interview_budget(update: Update, context):
    context.user_data['budget'] = update.message.text
    name = context.user_data['name']
    project = context.user_data['project']
    budget = context.user_data['budget']
    
    # Send the interview result to the creator's chat
    interview_msg = (
        f"📋 *New Interview Lead*\n"
        f"Name: {name}\n"
        f"Project: {project}\n"
        f"Budget/Timeline: {budget}\n"
        f"From: @{update.effective_user.username or 'no username'}"
    )
    await context.bot.send_message(chat_id=CREATOR_CHAT_ID, text=interview_msg, parse_mode="Markdown")
    
    await update.message.reply_text(
        "✅ *Thank you!* Douglas will review your info and reach out shortly.\n\n"
        "In the meantime, you can ask me about specs, experience, or use /help.",
        parse_mode="Markdown"
    )
    return ConversationHandler.END

async def cancel(update: Update, context):
    await update.message.reply_text("Interview cancelled. Type /start to begin again.")
    return ConversationHandler.END

# ========== CALLBACK QUERY HANDLER ==========
async def button_callback(update: Update, context):
    query = update.callback_query
    await query.answer()
    data = query.data
    if data == "experience":
        await query.edit_message_text(BIO, parse_mode="Markdown")
    elif data == "specs":
        await query.edit_message_text(SPECS, parse_mode="Markdown")
    elif data == "interview":
        await query.edit_message_text(
            "🎤 *Starting interview...*\n\n"
            "What’s your *full name*?",
            parse_mode="Markdown"
        )
        return NAME
    elif data == "contact":
        await query.edit_message_text(
            "📧 *Email:* owensonicinfinity@gmail.com\n"
            "📱 *Phone:* 440-281-6270\n"
            "🌐 *GitHub:* owensonicinfinity.netlify.app\n\n"
            "Douglas usually replies within 24 hours.",
            parse_mode="Markdown"
        )
    # For interview flow via callback, we need to start conversation
    if data == "interview":
        return NAME
    return ConversationHandler.END

# ========== MAIN ==========
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("experience", experience))
    app.add_handler(CommandHandler("specs", specs))
    app.add_handler(CommandHandler("contact", contact))
    
    # Conversation handler for interview
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("interview", lambda u,c: interview_start(u,c)),
            CallbackQueryHandler(button_callback, pattern="^interview$")
        ],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, interview_name)],
            PROJECT: [MessageHandler(filters.TEXT & ~filters.COMMAND, interview_project)],
            BUDGET: [MessageHandler(filters.TEXT & ~filters.COMMAND, interview_budget)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler)
    
    # Handle button callbacks
    app.add_handler(CallbackQueryHandler(button_callback))
    
    # Echo any other message to the creator (optional)
    async def echo(update, context):
        if update.message.text and not update.message.text.startswith('/'):
            await context.bot.send_message(
                chat_id=CREATOR_CHAT_ID,
                text=f"💬 From @{update.effective_user.username}: {update.message.text}"
            )
            await update.message.reply_text("Message forwarded to Douglas. He'll reply soon.")
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("🤖 DaisyAI Vortex bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
```

---

🚀 How to Run the Bot

Option A: On Your Own Computer (for testing)

1. Install Python if not already.
2. Install the library:
      pip install python-telegram-bot==20.7
3. Replace YOUR_BOT_TOKEN_HERE and YOUR_CHAT_ID_HERE in the script.
4. Run:
      python daisy_bot.py
5. Keep the terminal open. The bot will now respond.

Option B: Free Cloud Hosting (24/7)

I recommend Render (free tier):

1. Push this script to a GitHub repository.
2. Sign up at render.com → New Web Service → Connect GitHub.
3. Build command: pip install python-telegram-bot
4. Start command: python daisy_bot.py
5. Add environment variables BOT_TOKEN and CREATOR_CHAT_ID (more secure).
6. Deploy – it stays alive.

---

🧪 Test the Bot

1. Open Telegram → search @DAISYAIVORTEXbot
2. Send /start – you’ll see the persona menu.
3. Click “My Experience” – your full bio appears.
4. Click “Start Interview” – the bot asks name, project, budget. All answers are forwarded to your personal Telegram chat.
5. Send any message (not a command) – the bot forwards it to you, so you can reply manually.

---

🔗 Connect to Your HTML Page

Your HTML already has the Telegram bubble pointing to https://t.me/DAISYAIVORTEXbot. Once the bot is running, visitors will get this interactive experience.

---

✅ Next Steps (Immediate)

1. Run the BotFather commands to set description, about, and profile picture.
2. Copy the token and your chat ID into the Python script.
3. Run the script locally to test.
4. Deploy to Render for 24/7 uptime.
5. Test the interview flow yourself.

Your bot will now represent DaisyAI, answer with your full background, and capture leads automatically.

Want me to help you deploy it step-by-step on Render? Or adjust the persona/interview questions further?
