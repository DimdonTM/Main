import socket
import webbrowser
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 1234))
server.listen()
while True:
    user, adres = server.accept()
    while True:
        data = user.recv(1024).decode("utf-8").lower()
        print(data)
        # Ссылки
        if data == "yt":
            webbrowser.open("https://www.youtube.com")

