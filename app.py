import logging
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# 設定您的 Telegram Bot 的 token
TOKEN = "Your Token"

# 設定轉發訊息的目標群組 ID
TARGET_GROUP_ID = "Target ID"

# 設定日誌紀錄的等級
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# 定義一個處理訊息的函數，當 Bot 收到訊息時，會呼叫此函數
def forward_message(update: Update, context: CallbackContext):
    # 當前訊息的Json檔
    message = update.effective_message 
    # 取得目前訊息所在的群組或頻道 ID
    chat_title = message['chat']['title']
    chat_id = message.chat_id

    # 如果訊息中包含媒體檔案才執行轉發
    if message.media_group_id or message.photo or message.video or message.document:

        # 如果媒體檔案有名稱 回傳名稱
        file_name = message.document.file_name if message.document else None

        # 將訊息轉發到目標群組
        context.bot.send_message(chat_id=TARGET_GROUP_ID, text="Received message from " + chat_title)
        if file_name:
            print(f"Document file name: {file_name}")
            context.bot.send_message(chat_id=TARGET_GROUP_ID, text="Document file name: "+ file_name)

        context.bot.forward_message(chat_id=TARGET_GROUP_ID, from_chat_id=chat_id, message_id=message.message_id)
        # 在控制台上輸出該群組的 ID 或頻道的 ID
        # print(f"Received message from {chat_title}, {chat_id}")
        print(f"Received message from {chat_title}")


# 建立一個 Telegram Bot 實例
bot = Updater(token=TOKEN, use_context=True)

# 設定一個 MessageHandler 實例，處理所有來自群組或頻道的訊息
bot.dispatcher.add_handler(MessageHandler(Filters.chat_type.groups | Filters.chat_type.channel, forward_message))

# 啟動 Bot，開始接收訊息
bot.start_polling()

# 讓 Bot 一直運行，直到程式被手動停止
bot.idle()
