import socket
from conftest import db_connection
from helpers import random_string, random_email, random_phone
from config import config

password = "$2y$10$Ra9Adr9RCviSWdiwDTRXT.drmQE0A0P7z6aS5dcDXbPnf7tRSlNf." # test

def test_create_user_to_table_oc_customer(db_connection):
    """Сщздание нового клиента в таблице oc_customer. Пароль зашит как 'test'"""

    query_insert = ('INSERT INTO `oc_customer` (`customer_id`, `customer_group_id`, `store_id`, `language_id`, `firstname`, '
             '`lastname`, `email`, `telephone`, `password`, `custom_field`, `newsletter`, `ip`, `status`, `safe`, '
             '`token`, `code`, `date_added`) VALUES (NULL, 1, 0, 1, %s, %s, %s, %s, %s, "", 0, %s, 1, 1, "", "", NOW());')

    email = random_email()
    ip = socket.gethostbyname(socket.gethostname())

    cursor = db_connection.cursor()
    cursor.execute(query_insert, (
                        random_string(),
                        random_string(),
                        email, random_phone(), password, ip,))
    db_connection.commit()

    query_read = f"SELECT customer_id FROM {config.TABLE} WHERE email='{email}'"

    cursor.execute(query_read)
    result = cursor.fetchone()  # Получаем первую строку результата
    customer_id = result[0] if result else None

    print(f"Создан email: {email}, пароль: test, customer_id: {customer_id}")

    # Проверка: клиент должен существовать в базе
    assert customer_id is not None, f"Клиент c email= {email} не найден в базе"
