from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import anthropic
import os

load_dotenv()

# ── Placeholders ──────────────────────────────────────────────────────────────
TOKEN: Final = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN_HERE")
ANTHROPIC_API_KEY: Final = os.getenv("ANTHROPIC_API_KEY", "YOUR_ANTHROPIC_API_KEY_HERE")
BOT_USERNAME: Final = "@LegalCodebreakerBot"
# ─────────────────────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are a Singapore legal information assistant. Your role is to help users
understand the Singaporean legal system clearly and accurately.

Guidelines:
- Only answer questions related to Singapore law, legislation, and the judiciary.
- Always cite your sources explicitly — include the specific Act, section number, penal code,
  or official URL where the information was found (e.g. sso.agc.gov.sg, judiciary.gov.sg,
  mlaw.gov.sg, cpib.gov.sg).
- Prefer official Singapore government sources: Singapore Statutes Online (SSO), the
  Singapore Judiciary website, the Attorney-General's Chambers, Ministry of Law, etc.
- Quote the relevant section or clause when citing a statute or penal code.
- If a question falls outside Singapore law, politely decline and redirect the user.
- Always remind users that your answers are for informational purposes only and do not
  constitute legal advice. Encourage them to consult a qualified Singapore lawyer for
  matters requiring professional legal advice.
- Do not speculate or fabricate legal provisions. If you are unsure, say so clearly."""


client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


# ── Commands ──────────────────────────────────────────────────────────────────

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! I'm LegalCodebreaker, your Singapore legal information assistant.\n\n"
        "I can help you understand Singapore laws, statutes, penal codes, and the judiciary "
        "system — with cited sources from official Singapore government websites.\n\n"
        "⚠️ Note: I provide legal information, not legal advice. Always consult a qualified "
        "lawyer for matters requiring professional guidance.\n\n"
        "Ask me anything about Singapore law!"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ *How to use this bot:*\n\n"
        "Simply ask any question about Singapore law and I'll do my best to answer "
        "with cited sources from official Singapore government websites.\n\n"
        "*Example questions:*\n"
        "• What is the penalty for drug trafficking in Singapore?\n"
        "• What are my rights if I'm arrested?\n"
        "• What does the Misuse of Drugs Act cover?\n\n"
        "For professional legal advice, please consult a qualified Singapore lawyer or "
        "visit the Law Society of Singapore at lawsociety.org.sg.",
        parse_mode="Markdown"
    )


# ── Core response logic ───────────────────────────────────────────────────────

def handle_response(text: str) -> str:
    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            tools=[{"type": "web_search_20250305", "name": "web_search"}],
            messages=[
                {"role": "user", "content": text}
            ]
        )

        # Extract the text content from the response
        reply_parts = []
        for block in response.content:
            if block.type == "text":
                reply_parts.append(block.text)

        return "\n".join(reply_parts) if reply_parts else "I was unable to generate a response. Please try again."

    except anthropic.APIConnectionError:
        return "⚠️ I'm having trouble connecting to my knowledge service. Please try again shortly."
    except anthropic.RateLimitError:
        return "⚠️ I'm receiving too many requests right now. Please wait a moment and try again."
    except anthropic.APIStatusError as e:
        print(f"Anthropic API error: {e.status_code} — {e.message}")
        return "⚠️ An error occurred while processing your request. Please try again."


# ── Message handler ───────────────────────────────────────────────────────────

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: {text}")

    if message_type == "group":
        if BOT_USERNAME in text:
            text = text.replace(BOT_USERNAME, "").strip()
        else:
            return  # Ignore group messages that don't mention the bot

    # Show "typing..." indicator while processing
    await context.bot.send_chat_action(
        chat_id=update.message.chat_id,
        action="typing"
    )

    response = handle_response(text)

    print(f"Bot: {response}")
    await update.message.reply_text(response)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error: {context.error}")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Starting LegalCodebreaker bot...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error_handler)

    print("Polling started...")
    app.run_polling(poll_interval=1)
