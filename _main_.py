# Модули
import webbrowser, os, subprocess, time
from pathlib import Path

# Читает и записывает содержимое текстовых файлов, где находятся токен и таймер
def _read():
    global _token_, _timer_
    with open(".libraly/.txt/_token_.txt", "r", encoding="utf-8") as f:
        _token_ = f.read()
    with open(".libraly/.txt/_timer_.txt", "r", encoding="utf-8") as f:
        _timer_ = f.read()

# Очистка
def clear():
    if os.name == "nt": # если система Windows (nt), то использует cls. Если нет (Linux, macOS), то clear
        os.system("cls")
    else:
        os.system("clear")

# Меню
while True:
    clear()
    _read()
    print("<---------------------->")
    print("[1] - скачать zapret")
    print("[2] - токен или таймер")
    print("[3] - авторы")
    print("[0] - выход")
    print("<---------------------->")
    _answerUser=input("> ")
    match _answerUser:
        case "1": # переход в каталог
            if _token_ != "": # проверка на существования токена
                subprocess.run(["python", ".libraly\.py\_catalog_.py"])
            else:
                clear()
                print("Сначало введите токен!")
                time.sleep(2)

        case "2":
            clear()
            print(f"[1] Токен: {_token_}")
            print(f"[2] Таймер: {_timer_}")
            print("~ если ничего не хотите менять, просто нажмите Enter")
            print("~ подробнее про токен или таймер - read")
            _answerUser=input("> ")
            if _answerUser != "":
                match _answerUser:
                    case "1":
                        clear()
                        _answerUser=input("Введите ваш токен: ")
                        # Файлы открыты в режиме "w", чтобы они каждый раз перезаписывали файл с новой информацией (так проще)
                        with open(".libraly/.txt/_token_.txt", "w", encoding="utf-8") as f:
                            f.write(_answerUser)
                    case "2":
                        clear()
                        _answerUser=input("Введите количество секунд: ")
                        with open(".libraly/.txt/_timer_.txt", "w", encoding="utf-8") as f:
                            f.write(_answerUser)
                    case "read":
                        clear()
                        webbrowser.open("https://github.com/blohoped/Zapret-Catalog?tab=readme-ov-file#-%D1%82%D0%BE%D0%BA%D0%B5%D0%BD")

        case "3":
            clear()
            print("<-------------------->")
            print("[1] - автор zapret")
            print("[2] - автор каталога")
            print("<-------------------->")
            _answerUser=input("> ")
            match _answerUser:
                case "1":
                    webbrowser.open("https://github.com/Flowseal")
                case "2":
                    webbrowser.open("https://github.com/blohoped")

        case "0":
            break