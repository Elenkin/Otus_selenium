from config import config
from helpers import create_user_and_get_customer_id, random_string, random_email, random_phone


def test_update_user(db_connection):
    customer_id = create_user_and_get_customer_id(db_connection)
    print(f"Создан customer_id: {customer_id}")

    new_firstname = random_string()
    new_lastname = random_string()
    new_email = random_email()
    new_telephone = random_phone()

    update_query = f"""
        UPDATE {config.TABLE}
        SET firstname = %s, lastname = %s, email = %s, telephone = %s
        WHERE customer_id = %s
    """
    cursor = db_connection.cursor()
    cursor.execute(update_query, (new_firstname, new_lastname, new_email, new_telephone, customer_id))

    db_connection.commit()
    print(f"Выполнен запрос: {update_query} с параметрами: firstname={new_firstname}, lastname={new_lastname}, "
                                                            f"email={new_email}, telephone={new_telephone}")

    # Проверка: Выполняем запрос в табл по customer_id
    check_query = f"SELECT firstname, lastname, email, telephone FROM {config.TABLE} WHERE customer_id = %s"
    cursor.execute(check_query, (customer_id,))
    result = cursor.fetchone()

    assert result is not None, "Клиент не найден"
    # Распаковка результата
    db_firstname, db_lastname, db_email, db_telephone = result

    assert db_firstname == new_firstname, f"Ожидалось firstname = {new_firstname}, но {db_firstname}"
    assert db_lastname == new_lastname, f"Ожидалось lastname = {new_lastname}, но {db_lastname}"
    assert db_email == new_email, f"Ожидалось email = {new_email}, но {db_email}"
    assert db_telephone == new_telephone, f"Ожидалось telephone = {new_telephone}, но {db_telephone}"

def test_update_non_exist_customer(db_connection):
    """
    Негативный тест: попытка обновить клиента с несуществующим customer_id.
    Ожидается: никаких изменений в базе.
    """
    # Задаём не существующий customer_id
    non_exist_customer_id = 999999

    # Новые данные для обновления
    new_firstname = "Fake"
    new_lastname = "User"
    new_email = "fakeuser@example.com"
    new_telephone = "0000000000"

    # Пытаемся обновить клиента
    update_query = """
        UPDATE oc_customer
        SET firstname = %s, lastname = %s, email = %s, telephone = %s
        WHERE customer_id = %s
    """
    cursor = db_connection.cursor()
    cursor.execute(update_query, (new_firstname, new_lastname, new_email, new_telephone, non_exist_customer_id))
    db_connection.commit()

    # Проверка: строк должно быть обновлено 0
    assert cursor.rowcount == 0, f"Ожидалось 0 обновлённых строк, но обновлено: {cursor.rowcount}"

    # Дополнительно: убеждаемся, что таких данных в таблице нет
    check_query = "SELECT * FROM oc_customer WHERE customer_id = %s"
    cursor.execute(check_query, (non_exist_customer_id,))
    result = cursor.fetchone()

    assert result is None, "Найден клиент, которого не должно существовать"
