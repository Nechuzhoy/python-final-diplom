import requests

# регистрация пользователя
# response = requests.post(
#     'http://127.0.0.1:8000/api/v1/user/register',
#             json={"first_name": "Виктор",
#                   "last_name": "Иванов",
#                   "email": "test22@gmail.com",
#                   "password": "Ws9475098",
#                   "company": "Связной",
#                   "position": "1"
#             }
# )
#
# print(response.status_code)
# print(response.json())

# активация пользователя
# response = requests.post(
#     'http://127.0.0.1:8000/api/v1/user/register/confirm',
#             json={ "key": "a86aaf276cf6ce4f775"}
# )
#
# print(response.status_code)
# print(response.json())

# получение токена
# response = requests.post(
#     'http://127.0.0.1:8000/api/v1/user/login',
#             json={"email": "test3@gmail.com", "password":"Ws9475098"}
# )
#
# print(response.status_code)
# print(response.json())

# создать контакт!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# response = requests.post(
#     'http://127.0.0.1:8000/api/v1/user/contact/',
#     headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
#     json={'city': 'Москва',
#           'street': 'Нородного-Ополчения',
#           'house': '1',
#           'structure': '2',
#           'building': '3',
#           'apartment': '4',
#           'phone': '+791231232323',
#           'user': '1'
#           }
# )
#
# print(response.status_code)
# print(response.json())


# получение данных контакт
# response = requests.get(
#            'http://127.0.0.1:8000/api/v1/user/contact',
#     headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"}
# )
#
# print(response.status_code)
# print(response.json())

# редактирование данных контакт
# response = requests.put('http://127.0.0.1:8000/api/v1/user/contact/1/',
#     headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
#     json={
#                 "id": 1,
#                 "city": "Москва",
#                 "street": "Нородного-Ополчения",
#                 "house": "2",
#                 "structure": "2",
#                 "building": "3",
#                 "apartment": "4",
#                 "phone": "+791231232323"
#         }
# )
#
# print(response.status_code)
# print(response.json())

# удаление контакт
# response = requests.delete('http://127.0.0.1:8000/api/v1/user/contact/1/',
#     headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"}
# )
#
# print(response.status_code)
# print(response.json())


# обновить прайс
# response = requests.post('http://127.0.0.1:8000/api/v1/partner/update',
#     headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
#     json={
#     "url": "https://raw.githubusercontent.com/netology-code/pd-diplom/master/data/shop1.yaml"
# }
# )
#
# print(response.status_code)
# print(response.json())


# получить статус партнера
# response = requests.get('http://127.0.0.1:8000/api/v1/partner/state',
#     headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
#     json={
#     "url": "https://raw.githubusercontent.com/netology-code/pd-diplom/master/data/shop1.yaml"
# }
# )
#
# print(response.status_code)
# print(response.json())


# получить заказы
# response = requests.get('http://127.0.0.1:8000/api/v1/partner/orders',
#     headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
#     json={
#     "url": "https://raw.githubusercontent.com/netology-code/pd-diplom/master/data/shop1.yaml"
# }
# )
#
# print(response.status_code)
# print(response.json())


# обновить статус партнера
# response = requests.post('http://127.0.0.1:8000/api/v1/partner/update',
#     headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
#     json={
#     "state": "on"
# }
# )
#
# print(response.status_code)
# print(response.json())


# список магазинов
# response = requests.get('http://127.0.0.1:8000/api/v1/shops',)
#   headers = {"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
#
# print(response.status_code)
# print(response.json())


# просмотр категорий товара
# response = requests.get('http://127.0.0.1:8000/api/v1/categories')
#    headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
# print(response.status_code)
# print(response.json())


# просмотр товара
# response = requests.get('http://127.0.0.1:8000/api/v1/products')
#    headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
# print(response.status_code)
# print(response.json())

# добавление товара в корзину
# response = requests.post('http://127.0.0.1:8000/api/v1/basket',
#                          headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
#                          json={"items": '[{"product_info": 3, "quantity": 2}]'
#                                })
#
#
# print(response.status_code)
# print(response.json())

# изменение количества товара в корзине

# response = requests.put('http://127.0.0.1:8000/api/v1/basket',
#  headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
#                         json={'items':
#                                   '[{"id": 1,"quantity": 1}]'
#                               }
#                         )
# print(response.status_code)
# print(response.json())

# удаление товара из корзины
# response = requests.delete('http://127.0.0.1:8000/api/v1/basket',
#  headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
#                         json={'items':
#                                   '[{"id": 1}]'
#                               }
#                         )
# print(response.status_code)
# print(response.json())

# содержание корзина
# response = requests.get('http://127.0.0.1:8000/api/v1/basket',
#  headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"})
#
# print(response.status_code)
# print(response.json())

# оформление заказа
# response = requests.post('http://127.0.0.1:8000/api/v1/order',
#                     headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
#                     json={"id": "1", "contact":"1"})
# print(response.status_code)
# print(response.json())




# просмотр заказов
# response = requests.get('http://127.0.0.1:8000/api/v1/order',
#         headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"})
#
# print(response.status_code)
# print(response.json())
