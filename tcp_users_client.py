import socket

# Создаем TCP-сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
client_socket.connect(('localhost', 12345))

# Отправляем сообщение серверу
client_socket.send("Привет, сервер".encode())

# Получаем ответ от сервера
response = client_socket.recv(1024).decode()

# Закрываем соединение
client_socket.close()
