# ⚖️ LegalCodebreaker

A mobile-first application that helps laypersons understand Singapore's legal system and navigate it with confidence — from looking up statutes and penal codes to tracking upcoming court dates.

> ⚠️ LegalCodebreaker provides **legal information**, not legal advice. Always consult a qualified Singapore lawyer for matters requiring professional legal counsel.

---

## 📦 Project Structure

```
LegalCodebreaker/
├── Chatbot.py          # Telegram chatbot (Python)
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── App/                # Kotlin-based Android application
│   └── App.zip
└── Design/
    └── Hifi.xd         # Adobe XD high-fidelity mockups
```

---

## ✨ Features

### 🤖 Telegram Chatbot (`Chatbot.py`)
An AI-powered chatbot that answers questions about the Singapore legal system.

- Powered by **Claude (Anthropic)** with live web search
- Responses are grounded in official Singapore government sources:
  - [Singapore Statutes Online (SSO)](https://sso.agc.gov.sg)
  - [Singapore Judiciary](https://www.judiciary.gov.sg)
  - [Attorney-General's Chambers](https://www.agc.gov.sg)
  - [Ministry of Law](https://www.mlaw.gov.sg)
  - [CPIB](https://www.cpib.gov.sg)
- Cites specific Acts, section numbers, and penal codes in every response
- Refuses to speculate or answer questions outside Singapore law
- Reminds users to seek professional legal advice where appropriate

### 📱 Android App (`App.zip`)
A Kotlin-based native Android application.

**Court Date Notification System**
- Notifies users of upcoming court hearings they are required to attend
- Provides procedural guidance specific to each court attendance type (e.g. Mentions, Pre-Trial Conferences, Trials)
- Surfaces relevant general information to help users prepare

**Legal Information Hub**
- Browse Singapore statutes and legal topics in plain language
- Searchable legal reference content

### 🎨 HiFi Design (`Hifi.xd`)
High-fidelity mockups built in Adobe XD covering the full user experience of the Android application.

---

## 🚀 Getting Started (Telegram Bot)

### Prerequisites
- Python 3.10+
- A [Telegram Bot Token](https://core.telegram.org/bots/tutorial) from BotFather
- An [Anthropic API Key](https://console.anthropic.com)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/legalcodebreaker.git
   cd legalcodebreaker
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the project root:
   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

4. **Run the bot**
   ```bash
   python Chatbot.py
   ```

---

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `TELEGRAM_BOT_TOKEN` | Token from Telegram's BotFather |
| `ANTHROPIC_API_KEY` | API key from [console.anthropic.com](https://console.anthropic.com) |

A `.env.example` template is included in the repository. Copy it to `.env` and fill in your values — never commit your actual `.env` file.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Chatbot | Python, `python-telegram-bot` |
| AI / LLM | Anthropic Claude (`claude-sonnet-4`) with web search |
| Android App | Kotlin |
| UI Design | Adobe XD |

---

## 📋 Bot Commands

| Command | Description |
|---|---|
| `/start` | Introduction and onboarding message |
| `/help` | Usage guide and example questions |

---

## 🗺️ Roadmap

- [ ] Integrate chatbot AI into the Android app natively
- [ ] Add support for case status lookup via eLitigation
- [ ] Push notifications for court date reminders
- [ ] Multilingual support (Mandarin, Malay, Tamil)
- [ ] Lawyer directory / referral feature

---

## ⚠️ Disclaimer

LegalCodebreaker is intended for **informational purposes only**. The information provided does not constitute legal advice and should not be relied upon as such. For any legal matter, please consult a qualified lawyer licensed in Singapore. You may find one through the [Law Society of Singapore](https://www.lawsociety.org.sg).

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.
