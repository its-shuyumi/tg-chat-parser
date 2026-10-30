# 💬 TG Chat Parser

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)]()
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)]()

*Обычный упрощающий жизнь скрипт который поможет вам и вашему ИИ-агенту для анализа динамики общения, перспективы и прочего.*

*Делает удобный файл вида:*
```bash
2026-07-31
[20:24]              Я: вечерочка
[20:24] Павел Богданыч: Привеет
[20:24] Павел Богданыч: Как дела ?

```

[English](#-english) • [Русский](#-русский)


---

## 🇺🇸 English

### ✨ Features
- **Auto-Discovery:** Automatically scans your Telegram Desktop downloads folder, finds the freshest export for today, and grabs `result.json` seamlessly.
- **Smart Text Handling:** Correctly merges split text blocks and normalizes line breaks.
- **Clean Formatting:** Automatically detects your ID, replaces it with a custom `Я` tag (aligned with the interlocutor's name length), and splits logs by date.

### ⚙️ Quick Start
1. Export your chat history from Telegram Desktop (in JSON format). It will automatically land in your Downloads folder.
2. Run the script:
   ```bash
   python parser.py
3. Enter the exact name of the chat or user when prompted.
4. Find your clean chat log in `result.txt`!

---

## 🇷🇺 Русский



### ✨ Особенности

* **Автопоиск:** Скрипт сам сканирует папку загрузок Telegram Desktop, находит самый свежий экспорт за сегодня и подтягивает `result.json` без ручного ввода путей.
* **Умная склейка текста:** Корректно обрабатывает многострочные сообщения и составные блоки.
* **Кастомизация диалога:** Автоматически определяет ваш ID, заменяет его на маркер `Я` (с выравниванием по длине имени собеседника) и разделяет лог по датам.

### ⚙️ Быстрый старт

1. Сделайте экспорт истории чата в настройках Telegram Desktop (в формате JSON). Папка автоматически появится в ваших Загрузках.
2. Запустите скрипт:
    ```bash
    python parser.py

3. Заберите готовый структурированный лог в файле `result.txt` в корне проекта!

---
