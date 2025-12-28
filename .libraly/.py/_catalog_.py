# Модули
import webbrowser, os, subprocess, shutil, time
from github import Github, Auth
from pathlib import Path

# Читает и записывает содержимое текстовых файлов, где находятся токен и таймер
def _read():
    global _token_, _timer_
    with open(".libraly/.txt/_token_.txt", "r", encoding="utf-8") as f:
        _token_ = f.read()
    with open(".libraly/.txt/_timer_.txt", "r", encoding="utf-8") as f:
        _timer_ = f.read()

# База для всех zapret-ов
_base = {}

# Авторизация на Github
_read() # подгружает переменные
_auth = Auth.Token(_token_) # использует токен доступа
_g = Github(auth=_auth) # сайт github

# Получаем репозиторий
_repo = _g.get_repo("Flowseal/zapret-discord-youtube")

# Очистка
def clear():
    if os.name == "nt": # если система Windows (nt), то использует cls. Если нет (Linux, macOS), то clear
        os.system("cls")
    else:
        os.system("clear")

# Каталог
while True:
    clear()
    print("Все доступные zapret-ы:")
    print("<------------------------>")
    for number, release in enumerate(_repo.get_releases(), start = 1): # переменная number служит для простого подсчёта релизов, release служит для прогонки через себя всех релизов, а _repo.get_releases() - это список со всеми релизами, доступными в репозитории
        asset = release.assets[0] # переменная asset берёт первый asset(файл), и "запоминает" (записывает в себя)
        _regBase = { # это мини-словарик, который берёт страницу релиза (release.html_url), его тэга (release.tag_name), а также ссылку на скачивание первого asset-а (asset.browser_download_url)
            "release": release.tag_name,
            "url_web": release.html_url,
            "url_downoload": asset.browser_download_url
        }
        _base[release.tag_name] = _regBase # дальше, он записывает полученный мини-словарик с информацией о zapret-e под тэгом релиза, в базу zapret-ов

        print(f"{number}. {release.tag_name}") # пишем нумерацию и тэг каждой версии
    
    print("~ для выхода, напишите exit")

    _answerUser=input("> ")
    if _answerUser in _base:
        _saveData = _base[_answerUser] # для более простого обращения с ключами в мини-словаре, выводим мини-словарь в переменную
        clear()
        print(f"Все действия для релиза: {_saveData["release"]}")
        print("<---------------------------------------->")
        print(f"[1] - скачать zapret")
        print("[2] - открыть страницу zapret-а")
        print("<---------------------------------------->")
        print("~ для выхода нажмите Enter")
        _answerUser=input("> ")
        match _answerUser:
            case "1":
                # Наход пути скачанного файла
                webbrowser.open(_saveData["url_downoload"]) # открывает ссылку для скачивания
                time.sleep(int(_timer_)) # ждёт определённое время, пока браузер скачает файл
                _fileName = _saveData["url_downoload"].split("/")[-1] # переменная _fileName берёт из ключа "url_downoload" ссылку на ассет, потом режет ссылку на две части до последнего слэша (первую часть - выкидывает)
                _downloads_path = str(Path.home() / "Downloads") # потом переменная _downloads_path берёт путь к дому на компьютере, и соединяет с Downloads (чтобы получился путь к загрузкам)
                _shutilFile = os.path.join(_downloads_path, _fileName) # и наконец-то переменная _shutilFile с помощью функции os.path.join скрепляет путь Downloads и имя скачанного файла нужным для системы слэшем

                shutil.move(_shutilFile, "zapret") # и уже после этого, shutil.move перемещает файл по собранному пути в папку zapret
                
            case "2":
                webbrowser.open(_saveData["url_web"])

    elif _answerUser == "exit":
        subprocess.run(["python", "_main_.py"])
        break

    else:
        clear()
        print("В базе нет таких zapret-ов!")

        time.sleep(2)
