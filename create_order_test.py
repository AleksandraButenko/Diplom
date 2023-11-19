# Александра Бутенко, 10 когорта – финальный проект. Инженер по тестированию плюс
import data
import requests
import configuration



# Создание заказа
def post_new_order(body):
    # Запрос методом POST + URL + ручка
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER,
        json=body
    )

# Получение трэка
def get_order_from_track(track_number):
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER,
        # Запрос методом GET c передачей параметра t (трэкингового номера)
        params={'t': track_number}
    )


# Получение заказа по трэку заказа
def test_orders():
    # Создание заказа
    create_order_response = post_new_order(data.order_body)
    # Получение трэка из ответа на запрос
    track_number = create_order_response.json()["track"]
    # Передача трэкингового номера
    get_order_response = get_order_from_track(track_number)
    # Проверка кода ответа
    assert get_order_response.status_code == 200




