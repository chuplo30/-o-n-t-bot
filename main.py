import discord
from discord.ext import commands, tasks
import random, asyncio, threading
from flask import Flask, jsonify
from world import WORDS

CHANNEL_IDS = [1549102142902632478]
ROUND_TIMEOUT = 9999
HINT_AFTER = 45
HINT_REVEAL_CHARS = 3
PORT = 10000

print(f"Da load {len(WORDS)} tu")

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
bot = commands.Bot(command_prefix=".", intents=intents)

channels_state = {}


def normalize(text):
    return " ".join(text.lower().strip().split())


def pick_word(channel_id):
    st = channels_state.setdefault(channel_id, {"used": set()})
    available = [i for i, w in enumerate(WORDS) if i not in st["used"]]
    if not available:
        st["used"].clear()
        available = list(range(len(WORDS)))
    idx = random.choice(available)
    st["used"].add(idx)
    return WORDS[idx]


async def start_new_round(channel):
    cid = channel.id
    word = pick_word(cid)
    channels_state[cid].update({
        "word": word,
        "started_at": asyncio.get_event_loop().time(),
        "answered": False,
        "hinted": False,
    })
    embed = discord.Embed(
        title="DOAN TU",
        description=f"Goi y: **{word['hint']}**\n\nGo dap an vao kenh nay.",
        color=discord.Color.blue(),
    )
    embed.set_footer(text=f"{ROUND_TIMEOUT}s")
    await channel.send(embed=embed)


async def reveal_hint(channel):
    cid = channel.id
    st = channels_state.get(cid)
    if not st or st.get("answered") or "word" not in st:
        return
    ans = st["word"]["answer"]
    revealed = ans[:HINT_REVEAL_CHARS] + "..."
    await channel.send(f"Goi y them: bat dau bang **{revealed}** ({len(ans.split())} chu)")


@tasks.loop(seconds=1)
async def round_timer():
    now = asyncio.get_event_loop().time()
    for cid, st in list(channels_state.items()):
        word = st.get("word")
        if not word or st.get("answered"):
            continue
        elapsed = now - st["started_at"]

        if HINT_AFTER <= elapsed < HINT_AFTER + 1 and not st.get("hinted"):
            st["hinted"] = True
            ch = bot.get_channel(cid)
            if ch:
                await reveal_hint(ch)

        if elapsed >= ROUND_TIMEOUT:
            st["answered"] = True
            ch = bot.get_channel(cid)
            if ch:
                await ch.send(f"Het gio. Dap an: **{word['answer']}**")
                await asyncio.sleep(2)
                await start_new_round(ch)


@bot.event
async def on_ready():
    print(f"Bot online: {bot.user}")
    for cid in CHANNEL_IDS:
        ch = bot.get_channel(cid)
        if ch:
            await start_new_round(ch)
    if not round_timer.is_running():
        round_timer.start()


@bot.event
async def on_message(msg):
    if msg.author.bot:
        return
    if msg.channel.id not in CHANNEL_IDS:
        await bot.process_commands(msg)
        return

    st = channels_state.get(msg.channel.id)
    if not st or "word" not in st or st.get("answered"):
        await bot.process_commands(msg)
        return

    word = st["word"]
    if normalize(msg.content) == normalize(word["answer"]):
        st["answered"] = True
        try:
            await msg.add_reaction("\u2705")
        except discord.Forbidden:
            pass
        embed = discord.Embed(
            title="CHINH XAC",
            description=f"{msg.author.mention} doan dung: **{word['answer']}**",
            color=discord.Color.green(),
        )
        await msg.channel.send(embed=embed)
        await asyncio.sleep(2)
        await start_new_round(msg.channel)
    else:
        try:
            await msg.add_reaction("\u274c")
        except discord.Forbidden:
            pass

    await bot.process_commands(msg)


@bot.command(name="skid")
@commands.has_permissions(manage_messages=True)
async def cmd_skid(ctx):
    if ctx.channel.id not in CHANNEL_IDS:
        return
    st = channels_state.get(ctx.channel.id)
    if not st or "word" not in st:
        return
    await ctx.send(f"Bo qua. Dap an: **{st['word']['answer']}**")
    st["answered"] = True
    await start_new_round(ctx.channel)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Ban khong co quyen dung lenh nay.")
    elif isinstance(error, commands.CommandNotFound):
        return
    else:
        await ctx.send(f"Loi: {error}")


app = Flask(__name__)


@app.route("/")
def index():
    lines = []
    for cid in CHANNEL_IDS:
        st = channels_state.get(cid)
        if st and st.get("word"):
            lines.append(st["word"]["hint"])
        else:
            lines.append("chua co")
    return "\n".join(lines)


@app.route("/hint")
def hint():
    cid = CHANNEL_IDS[0]
    st = channels_state.get(cid)
    if not st or not st.get("word"):
        return "chua co"
    return st["word"]["hint"]


@app.route("/all")
def all_hints():
    data = {}
    for cid in CHANNEL_IDS:
        st = channels_state.get(cid)
        data[str(cid)] = st["word"]["hint"] if st and st.get("word") else None
    return jsonify(data)


def run_flask():
    app.run(host="0.0.0.0", port=PORT, debug=False, use_reloader=False)


if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    bot.run(os.getenv("TOKEN"))
