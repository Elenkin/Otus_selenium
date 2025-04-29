import socket

address_and_port = ("192.168.31.46", 40401)

# Запрос Клиента
http_request = (
        f"GET /?status=1010  HTTP/1.0\r\n"
        f"Host: 192.168.31.46\r\n"
        f"User-Agent: CustomClient/1.0\r\n"
        f"Accept: */*\r\n"
        f"Content-Type: application/json\r\n"
        f"\r\n"
        )

def sendclient_data_stream(socket):
    try:
        socket.send(http_request.encode())  # Отправляем весь запрос
        response = b"" #байтовая строка
        while True:
            data = socket.recv(4096)  # Получаем ответ от сервера
            if not data:
                break
            response += data
        return response.decode()
    except Exception as e:
        return f"Ошибка при обмене данными: {e}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(address_and_port)
    response = sendclient_data_stream(s)
print(response)