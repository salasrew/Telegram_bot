import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# 配置日誌
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# 定義處理 /start 命令的函式
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

# 定義處理 /echo 命令的函式
def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

# 定義處理非命令訊息的函式
def handle_message(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


# 創建一個 Updater 對象，並將其與憑證和代理配置一起使用（如果需要）
# 這裡使用的是長輪詢方式，如果您想使用 Webhook 方式，可以刪除 webhook_url 參數
updater = Updater(token='Your Token', use_context=True)

# 獲取 Dispatcher 物件
dispatcher = updater.dispatcher

# 添加處理 /start 命令的處理函式
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# 添加處理 /echo 命令的處理函式
echo_handler = CommandHandler('echo', echo)
dispatcher.add_handler(echo_handler)

# 添加處理非命令訊息的處理函式
message_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
dispatcher.add_handler(message_handler)

# 開始接收和分派訊息
updater.start_polling()

# 進入持續運行狀態
updater.idle()




