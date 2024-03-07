# Пример API-сервиса для магазина
# Пример документации API на основе базового примера дипломного проекта


## **Получить исходный код**

    git config --global user.name "YOUR_USERNAME"
    
    git config --global user.email "your_email_address@example.com"
    
    mkdir ~/my_diplom
    
    cd my_diplom
    
    git clone git@github.com:A-Iskakov/netology_pd_diplom.git
    
    cd netology_pd_diplom
    
    sudo pip3 install  --upgrade pip
    
    sudo pip3 install -r requirements.txt
    
    python3 manage.py makemigrations
     
    python3 manage.py migrate
    
    python3 manage.py createsuperuser    
    
 
## **Проверить работу модулей**
    
    
    python3 manage.py runserver 127.0.0.1:8000

## Вариант 2
# запуск базы данных
   docker-compose up -d pgdb
# проверка запуска базы данных
   docker ps -a
# создать образ на основе Dockerfile
   docker compose build
# запуск приложения 
   docker compose up



# Точки входа API сервиса

# Пример API Сервиса для магазина

### Вход
Аргументы для отправки API запроса
 * поля
   - Email
   - Пароль


### Регистрация
Аргументы для отправки API запроса
 * поля
   - Фамилия
   - Имя
   - Email
   - Пароль

### Запрос списка товаров с возможностью фильтрации и поиска

### JSON поля товара
 * наименование 
 * описание
 * поставщик 
 * характеристики 
 * цена 
 * количество

### Корзина с возможностью добавления и удаления товаров
Список товаров с полями
 * Наименование товара
 * Магазин 
 * Цена
 * Количество 
 * Сумма 



### API запрос добавления контакта
 * Аргументы для отправки 
   - Фамилия
   - Имя
   - Отчество
   - Email
   - Телефон
   - Адрес
     + Город
     + Улица
     + Дом
     + Корпус
     + Строение
     + Квартира

 
### API запрос на подтверждение заказа
 * ID корзины
 * ID контакта


###  Получение статуса и истории заказов
             

 * Номер
 * Дата
 * Сумма
 * Статус
    
## 

# регистрация пользователя
response = requests.post(
    'http://127.0.0.1:8000/api/v1/user/register',
            json={"first_name": "Виктор",
                  "last_name": "Иванов",
                  "email": "test22@gmail.com",
                  "password": "Ws9475098",
                  "company": "Связной",
                  "position": "1"
            }
)



# активация пользователя
response = requests.post(
    'http://127.0.0.1:8000/api/v1/user/register/confirm',
            json={ "key": "a86aaf276cf6ce4f775"}
)

# получение токена
response = requests.post(
    'http://127.0.0.1:8000/api/v1/user/login',
            json={"email": "test3@gmail.com", "password":"Ws9475098"}
)


# создать контакт
response = requests.post(
    'http://127.0.0.1:8000/api/v1/user/contact/',
    headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
    json={'city': 'Москва',
          'street': 'Нородного-Ополчения',
          'house': '1',
          'structure': '2',
          'building': '3',
          'apartment': '4',
          'phone': '+791231232323',
          'user': '1'
          }
)


# получение данных контакт
response = requests.get(
           'http://127.0.0.1:8000/api/v1/user/contact',
    headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"}
)


# редактирование данных контакт
response = requests.put('http://127.0.0.1:8000/api/v1/user/contact/1/',
    headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
    json={
                "id": 1,
                "city": "Москва",
                "street": "Нородного-Ополчения",
                "house": "2",
                "structure": "2",
                "building": "3",
                "apartment": "4",
                "phone": "+791231232323"
        }
)



# удаление контакт
response = requests.delete('http://127.0.0.1:8000/api/v1/user/contact/1/',
    headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"}
)




# обновить прайс
response = requests.post('http://127.0.0.1:8000/api/v1/partner/update',
    headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
    json={
    "url": "https://raw.githubusercontent.com/netology-code/pd-diplom/master/data/shop1.yaml"
}
)



# получить статус партнера
response = requests.get('http://127.0.0.1:8000/api/v1/partner/state',
    headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
    json={
    "url": "https://raw.githubusercontent.com/netology-code/pd-diplom/master/data/shop1.yaml"
}
)



# получить заказы
response = requests.get('http://127.0.0.1:8000/api/v1/partner/orders',
    headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
    json={
    "url": "https://raw.githubusercontent.com/netology-code/pd-diplom/master/data/shop1.yaml"
}
)




# обновить статус партнера
response = requests.post('http://127.0.0.1:8000/api/v1/partner/update',
    headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
    json={
    "state": "on"
}
)



# список магазинов
response = requests.get('http://127.0.0.1:8000/api/v1/shops',)
  headers = {"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},




# просмотр категорий товара
response = requests.get('http://127.0.0.1:8000/api/v1/categories')
   headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},



# просмотр товара
response = requests.get('http://127.0.0.1:8000/api/v1/products')
   headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},


# добавление товара в корзину
response = requests.post('http://127.0.0.1:8000/api/v1/basket',
                         headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
                         json={"items": '[{"product_info": 3, "quantity": 2}]'
                               })



# изменение количества товара в корзине

response = requests.put('http://127.0.0.1:8000/api/v1/basket',
 headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
                        json={'items':
                                  '[{"id": 1,"quantity": 1}]'
                              }
                        )


# удаление товара из корзины
response = requests.delete('http://127.0.0.1:8000/api/v1/basket',
 headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
                        json={'items':
                                  '[{"id": 1}]'
                              }
                        )

# содержание корзина
response = requests.get('http://127.0.0.1:8000/api/v1/basket',
 headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"})



# оформление заказа
response = requests.post('http://127.0.0.1:8000/api/v1/order',
                    headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"},
                    json={"id": "1", "contact":"1"})



# просмотр заказов
response = requests.get('http://127.0.0.1:8000/api/v1/order',
        headers={"Authorization": "Token e47ee35d74a616c45347d9a08cd92ba10071b1ea"})

