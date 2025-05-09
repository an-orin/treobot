from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Menu chính
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 *Danh sách game:*\n\n"
        "1. Liên Quân (/1)\n"
        "2. Free Fire (/2)\n"
        "3. PUBG Mobile (/3)\n"
    , parse_mode="Markdown")

# ——— Liên Quân ———
async def macro_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✦ *Liên Quân* — Chọn vai trò:\n\n"
        "1️⃣ Đỡ đòn (/1dodon)\n"
        "2️⃣ Đấu sĩ (/1dausi)\n"
        "3️⃣ Sát thủ (/1sathu)\n"
        "4️⃣ Pháp sư (/1phapsu)\n"
        "5️⃣ Xạ thủ (/1xathu)\n"
        "6️⃣ Trợ thủ (/1trothu)\n"
    , parse_mode="Markdown")

async def lienquan_dodon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💪 *Đỡ đòn*:\n- Toro\n- Mganga\n- Thane\n", parse_mode="Markdown")

async def lienquan_dausi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚔️ *Đấu sĩ*:\n- Wukong\n- Florentino\n- Rourke\n", parse_mode="Markdown")

async def lienquan_sathu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔪 *Sát thủ*:\n- Nakroth\n- Murad\n- Zill\n", parse_mode="Markdown")

async def lienquan_phapsu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔮 *Pháp sư*:\n- Lauriel\n- Ilumia\n- Diao Chan\n", parse_mode="Markdown")

async def lienquan_xathu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏹 *Xạ thủ*:\n- Valhein\n- Tel'Annas\n- Capheny\n", parse_mode="Markdown")

async def lienquan_trothu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡️ *Trợ thủ*:\n- Alice\n- Annette\n- Chaugnar\n", parse_mode="Markdown")

# ——— Free Fire ———
async def macro_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✦ *Free Fire* — Chọn nhân vật:\n\n"
        "1️⃣ Chrono (/2chrono)\n"
        "2️⃣ Alok (/2alok)\n"
        "3️⃣ Kelly (/2kelly)\n"
        "4️⃣ K (/2k)\n"
        "5️⃣ Hayato (/2hayato)\n", parse_mode="Markdown")

async def ff_chrono(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡️ *Chrono*\n- Tạo lá chắn năng lượng chặn sát thương và có thể tấn công ngược\n", parse_mode="Markdown")

async def ff_alok(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 *Alok*\n- Tạo hào quang tăng tốc độ di chuyển và hồi HP\n", parse_mode="Markdown")

async def ff_kelly(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏃 *Kelly*\n- Tăng tốc độ chạy khi chuyển hướng\n", parse_mode="Markdown")

async def ff_k(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✂️ *K*\n- Chuyển giữa 2 trạng thái: tăng sát thương cận chiến hoặc máu tối đa\n", parse_mode="Markdown")

async def ff_hayato(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚔️ *Hayato*\n- Tăng giáp xuyên qua mỗi 5% HP đã mất\n", parse_mode="Markdown")

# ——— PUBG Mobile ———
async def macro_3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✦ *PUBG Mobile* — Chọn loại vũ khí:\n\n"
        "1️⃣ AR (/3ar)\n"
        "2️⃣ SMG (/3smg)\n"
        "3️⃣ Sniper (/3sniper)\n"
        "4️⃣ Shotgun (/3shotgun)\n", parse_mode="Markdown")

async def pubg_ar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔫 *AR*:\n- M416\n- AKM\n- SCAR-L\n", parse_mode="Markdown")

async def pubg_smg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔫 *SMG*:\n- UMP45\n- Vector\n- MP5K\n", parse_mode="Markdown")

async def pubg_sniper(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔫 *Sniper*:\n- AWM\n- Kar98k\n- M24\n", parse_mode="Markdown")

async def pubg_shotgun(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔫 *Shotgun*:\n- S1897\n- S686\n- DBS\n", parse_mode="Markdown")

# ——— Main ———
if __name__ == '__main__':
    app = ApplicationBuilder().token("8054215411:AAHjlYpSFWGD5Y_FNA04P3B0ZDo_umWxLrE").build()

    # Menu
    app.add_handler(CommandHandler("menu", menu))

    # Liên Quân
    app.add_handler(CommandHandler("1", macro_1))
    app.add_handler(CommandHandler("1dodon", lienquan_dodon))
    app.add_handler(CommandHandler("1dausi", lienquan_dausi))
    app.add_handler(CommandHandler("1sathu", lienquan_sathu))
    app.add_handler(CommandHandler("1phapsu", lienquan_phapsu))
    app.add_handler(CommandHandler("1xathu", lienquan_xathu))
    app.add_handler(CommandHandler("1trothu", lienquan_trothu))

    # Free Fire
    app.add_handler(CommandHandler("2", macro_2))
    app.add_handler(CommandHandler("2chrono", ff_chrono))
    app.add_handler(CommandHandler("2alok", ff_alok))
    app.add_handler(CommandHandler("2kelly", ff_kelly))
    app.add_handler(CommandHandler("2k", ff_k))
    app.add_handler(CommandHandler("2hayato", ff_hayato))

    # PUBG Mobile
    app.add_handler(CommandHandler("3", macro_3))
    app.add_handler(CommandHandler("3ar", pubg_ar))
    app.add_handler(CommandHandler("3smg", pubg_smg))
    app.add_handler(CommandHandler("3sniper", pubg_sniper))
    app.add_handler(CommandHandler("3shotgun", pubg_shotgun))

    app.run_polling()