# Geolocation_Of_The_City

Программа, функционал которой предоставляет 
пользователю доступ к API сервиса dadata.ru, 
в частности - к функционалу подсказок адресов.

Ознакомиться с API сервиса можно по ссылке: https://dadata.ru/api/suggest/address/

Для получения API ключа и секретного ключа Вам необходимо 
зарегистрироваться в сервисе, после чего необходимые данные будут 
доступны в Вашем личном кабинете по ссылке: https://dadata.ru/profile/#info

Установка:
1. Склонируйте репозиторий
```
git clone git@github.com:Jon-Makkonahi/Geolocation_Of_The_City.git
```
2. Перейдем в него 
```
cd Geolocation_Of_The_City
```
3. Создайте и войдите в виртуальное окружение
```
python -m venv venv
```
```
source venv/Scripts/activate
```
4. Установите зависимости:
```
pip install -r requirements.txt
```
5. Перезапустите VScode и заново зайдите в виртуальное окружение, если программа показывает что зависимости не установились!
6. Создайте файл .env и вставьте туда строку
```
TOKEN='Cюда вставьте API-ключ который находится у вас в личном кабинете на сайте dadata.ru'
```
7. Запустите скрипт work_with_sqlite.py
8. Запустите программу  geolocation_of_the_city.py и пользуйтесь)
