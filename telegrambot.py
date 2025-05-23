from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# /start komandasi uchun funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    group_link = "https://t.me/nokis_tashken_almati"  # Guruh linkini shu yerga yozing
    keyboard = [
        [InlineKeyboardButton("👥 Guruhga qo‘shilish", url=group_link)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Assalomu alaykum!\n \nQuyidagi tugma orqali guruhimizga qo‘shiling: \n https://t.me/nokis_tashken_almati \n https://t.me/tashkent_nokis1",
        reply_markup=reply_markup
    )

# Botni ishga tushirish
async def main():
    app = ApplicationBuilder().token("7671456979:AAFHNMa8X1kG8zlc4M4Z2UYGn4ZT3w7k14Y").build()  # Bot tokenini yozing

    app.add_handler(CommandHandler("start", start))

    await app.run_polling()

# Asosiy funksiya chaqiriladi
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
