from pyrogram import Client, filters
from datetime import datetime
import requests

# ── Config ──────────────────────────────────────────────
API_ID     = "29647483"
API_HASH   = "06257cea0e99f7541e9faeba27306f7f"
BOT_TOKEN  = "8717937001:AAEBuLBECgmFwjMXX2a_B7okwKl3epaHXtM"
SHEETY_URL = "https://api.sheety.co/7bcc93f9555fe5ac4003c262a4f6963c/workoutTraker/sheet1"
# ────────────────────────────────────────────────────────

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


# ── /start ───────────────────────────────────────────────
@app.on_message(filters.command("start"))
async def start_handler(client, message):
    user_name = message.from_user.first_name
    await message.reply(
        "🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥\n"
        "⚡ **LET'S GET TO WORK!** ⚡\n"
        "🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥\n\n"
        f"YO **{user_name}**!! 💥\n"
        f"YOUR GRIND STARTS NOW! 😤💪\n\n"
        "🚀 NO PAIN. NO GAIN.\n"
        "💀 NO DAYS OFF.\n"
        "⚡ NO EXCUSES.\n\n"
        "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
        "HIT /help AND LET'S GOOO!! 🔥🔥"
    )


# ── /help ────────────────────────────────────────────────
@app.on_message(filters.command("help"))
async def help_handler(client, message):
    await message.reply(
        "💥 **WHAT CAN I DO?!** 💥\n"
        "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n\n"
        "🚀 /start    →  WAKE UP!!\n"
        "💡 /help     →  THIS SCREEN!\n"
        "🏋️ /traker  →  LOG THE GRIND!\n\n"
        "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
        "⚡ _EVERY REP COUNTS!! LET'S GO!!_ 🔥"
    )


# ── /traker ──────────────────────────────────────────────
@app.on_message(filters.command("traker"))
async def traker_handler(client, message):
    await message.reply(
        "💪 **TIME TO LOG YOUR GRIND!!** 💪\n"
        "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n\n"
        "SMASH that workout in!! 👇👇\n\n"
        "📋 FORMAT:\n"
        "`exercise  sets  weight  reps`\n\n"
        "🔥 EXAMPLE:\n"
        "`Pull-ups 3sets 20kg 6,6,5`\n\n"
        "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
        "⚡ _YOU GOT THIS!! SEND IT!!_ 😤🔥"
    )


# ── Text input ───────────────────────────────────────────
@app.on_message(filters.text)
async def text_handler(client, message):
    if message.text.startswith("/"):
        return

    user_input = message.text

    # Parse input into list
    lst  = []
    name = ""
    for word in user_input:
        if word != " ":
            name += word
        else:
            lst.append(name)
            name = ""
    lst.append(name)

    # lst[0] = exercise, lst[1] = sets, lst[2] = weight, lst[3] = reps
    if lst:
        date = f"{datetime.now().day}/{datetime.now().month}/{datetime.now().year}"

        data = {
            "sheet1": {
                "date":         date,
                "exerciseName": lst[0],
                "sets":         lst[1],
                "weight":       lst[2],
                "reps":         lst[3],
            }
        }

        response = requests.post(url=SHEETY_URL, json=data)

        if response.status_code == 200:
            await message.reply(
                "🔥🔥 **WORKOUT LOCKED IN!!** 🔥🔥\n"
                "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n\n"
                f"📅  **Date**      ⚡  {date}\n"
                f"🏋️  **Exercise**  ⚡  {lst[0]}\n"
                f"🔁  **Sets**      ⚡  {lst[1]}\n"
                f"🏋️  **Weight**    ⚡  {lst[2]}\n"
                f"💥  **Reps**      ⚡  {lst[3]}\n\n"
                "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
                "😤 _CRUSHED IT!! KEEP GOING!! YOU'RE UNSTOPPABLE!!_ 🚀🔥💪"
            )
        else:
            await message.reply(
                "😤 **SOMETHING WENT WRONG!!**\n"
                "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n\n"
                f"💀 Error Code: `{response.status_code}`\n\n"
                "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
                "⚡ _DON'T STOP!! TRY AGAIN!!_ 🔥"
            )


# ── Run ──────────────────────────────────────────────────
print("⚡🔥 BOT IS ALIVE AND READY TO GRIND!! 🔥⚡")
app.run()