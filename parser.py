import json
import os
import sys
from datetime import date

# ╔══════════════════════════════════════════════════════════════╗
# ║                       CONFIG & PATHS                         ║
# ╚══════════════════════════════════════════════════════════════╝

# ╔═ Пути к папкам загрузок Telegram Desktop ═╗
BASE_PATH = r"C:\Users\S H Y U Y M I\Downloads\Telegram Desktop"
TODAY_STR = f"DataExport_{date.today()}"
# ╚═════════════════════════════════════════╝


# ╔══════════════════════════════════════════════════════════════╗
# ║                       FILE DISCOVERY                         ║
# ╚══════════════════════════════════════════════════════════════╝

# ╔═ Автопоиск свежей папки экспорта за сегодня ═╗
  
  def find_latest_export():
    candidates = []
    if os.path.exists(BASE_PATH):
        for folder in os.listdir(BASE_PATH):
            if folder.startswith(TODAY_STR) and os.path.isdir(os.path.join(BASE_PATH, folder)):
                candidates.append(folder)

    if not candidates:
        print("✘ Не найдена ни одна папка с экспортом за сегодня.")
        sys.exit()

    latest_folder = sorted(candidates)[-1]
    print(f"📁 Выбрана папка: {latest_folder}\n")
    return os.path.join(BASE_PATH, latest_folder, "result.json")
# ╚══════════════════════════════════════════════╝


# ╔══════════════════════════════════════════════════════════════╗
# ║                      CHAT PROCESSING                         ║
# ╚══════════════════════════════════════════════════════════════╝

# ╔═ Парсинг чата и автоопределение твоего ID ═╗
def parse_chat_export():
    result_path = find_latest_export()

    try:
        with open(result_path, 'r', encoding="utf-8") as r:
            f = json.load(r)
    except json.JSONDecodeError as e:
        print(f"✘ Ошибка чтения JSON: {e}")
        sys.exit()

    target_chat_name = input("С кем переписки надо сохранить?\n")

    target_chat = None
    for chat in f["chats"]["list"]:
        if chat.get("name") == target_chat_name:
            target_chat = chat
            break

    if not target_chat:
        print(f"✘ Чат с именем '{target_chat_name}' не найден.")
        sys.exit()

    messages = sorted(target_chat.get("messages", []), key=lambda m: m["id"])

    senders_map = {}
    for message in messages:
        f_name = message.get("from")
        f_id = message.get("from_id")
        if f_id and f_name and f_name != target_chat_name:
            senders_map[f_id] = f_name

    my_id = None
    for f_id in senders_map:
        if f_id != target_chat_name: # на всякий случай
            my_id = f_id
            break
          
    if not my_id:
        print("⚠ Не удалось автоматически выделить твой ID, используется заглушка.")
        my_id = "unknown"

    data_buf = ""
    with open("result.txt", 'w', encoding="utf-8") as w:
        for message in messages:
            msg_id = message.get("id")
            if msg_id is None:
                continue

            text = message.get("text", "")
            if isinstance(text, list):
                text = ''.join(part if isinstance(part, str) else part.get("text", "") for part in text)
            text = text.replace('\n', ' ')

            date_now = message['date'][:10]
            if data_buf != date_now:
                w.write(f'\n{date_now}\n')
                data_buf = date_now

            time = message['date'][11:-3]
            sender = message.get("from", "неизвестно")

            if message.get("from_id") == my_id:
                w.write(f'[{time}]{" " * (len(target_chat_name))}Я: {text}\n')
            else:
                w.write(f'[{time}] {sender}: {text}\n')

    print("\n✅ Успешно сохранено в result.txt")
# ╚════════════════════════════════════════════╝


# ╔══════════════════════════════════════════════════════════════╗
# ║                           MAIN                               ║
# ╚══════════════════════════════════════════════════════════════╝

if __name__ == "__main__":
    parse_chat_export()
