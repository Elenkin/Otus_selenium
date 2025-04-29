from helpers import get_user_customer_id
from config import config


def test_delete_user(db_connection):
    """ Проверка что удаления существующего клиента"""
    customer_id = get_user_customer_id(db_connection)
    print(f"Создан customer_id: {customer_id}")

    # Формируем запрос удаления по customer_id
    delete_query = f"""
        DELETE FROM {config.TABLE}
        WHERE customer_id = %s
    """
    cursor = db_connection.cursor()
    cursor.execute(delete_query, (customer_id,))
    db_connection.commit()

    # Провеяем что таких данных в таблице нет
    check_query = f"SELECT * FROM {config.TABLE} WHERE customer_id = %s"
    cursor.execute(check_query, (customer_id,))
    result = cursor.fetchone()

    assert result is None, f"Найден клиент, который должен быть удалён с customer_id={customer_id}"

def test_delete_non_exist_user(db_connection):
    """
    Негативный тест: попытка удалить клиента с несуществующим customer_id.
    Ожидается: никаких изменений в базе.
    """
    # Задаём не существующий customer_id
    non_exist_customer_id = 999999

    # Формируем запрос удаления по customer_id
    delete_query = f"""
        DELETE FROM {config.TABLE}
        WHERE customer_id = %s
    """
    cursor = db_connection.cursor()

    count_query = f"SELECT COUNT(*) FROM {config.TABLE}"
    cursor.execute(count_query)

    #Получаем count перед DELETE
    count_before = cursor.fetchone()[0]
    print(f"Количество записей в бд до удаления: {count_before}")

    cursor.execute(delete_query, (non_exist_customer_id,))
    db_connection.commit()

    # Получаем count после DELETE
    cursor.execute(count_query)
    count_after = cursor.fetchone()[0]
    print(f"Количество записей в бд после удаления: {count_after}")

    # Проверка: количество строк не должно измениться
    assert count_before == count_after, f"Ожидалось {count_before} юзеров в бд, но после удаления {count_after}"
