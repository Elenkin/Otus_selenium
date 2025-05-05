import socket
from http import HTTPStatus
from urllib.parse import urlparse, parse_qs

address_and_port = ("192.168.31.240", 40401)

def handle_client_connection(client_socket, client_address):
    try:
        # Получаем данные от клиента
        request = client_socket.recv(1024).decode()
        print(f"Получен запрос от {client_address}:\n{request}")

        # Разбор метода (первая строка запроса)
        lines = request.splitlines()
        request_line = lines[0] if lines else ""
        method, url, http_version = request_line.split(" ", 2)  # Разделяем по первому и второму пробелу

        # Извлекаем параметры из строки запроса
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        # Проверяем, если есть параметр 'status' и он валиден
        status_code = HTTPStatus.OK  # По умолчанию ставим статус 200 OK
        if 'status' in query_params:
            status_value = query_params['status'][0]
            # Проверяем, если статус валиден, используем его
            try:
                status_code = HTTPStatus(int(status_value))
            except ValueError:
                status_code = HTTPStatus.OK  # если параметр не валидный то отдавать 200
            except AttributeError:
                status_code = HTTPStatus.OK  # если параметр не передан то отдавать 200

        # Список для хранения заголовков
        headers = []
        # Заголовки
        for line in lines[1:]:
            if ':' in line:
                header_name, header_value = line.split(":", 1)
                header_name = header_name.strip()
                header_value = header_value.strip()
                headers.append(f"{header_name}: {header_value}")

        # Формируем ответ
        http_response = (
            f"Request Method: {method}\r\n"
            f"Request Source: {client_address}\r\n"
            f"Response Status: {status_code.value} {status_code.phrase}\r\n" + "\n".join(headers)
        )

        # Отправляем ответ обратно клиенту
        client_socket.send(http_response.encode())
    except Exception as e:
        print(f"Ошибка при обработке запроса: {e}")
    finally:
        client_socket.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind(address_and_port)  # Адрес и порт сервера
    serverSocket.listen(10)
    print("Сервер запущен и ожидает подключения...", address_and_port)

    try:
        while True:
            client_socket, addr = serverSocket.accept()
            print(f"Подключение от {addr}")
            handle_client_connection(client_socket, addr)
    except KeyboardInterrupt:
        print("\nСервер остановлен вручную.")