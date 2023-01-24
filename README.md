1. Скачать git
2. В папке создать файл .env:
    - `POSTGRES_DB=` Имя db
    - `POSTGRES_USER=` Имя
    - `POSTGRES_PASSWORD=` Пароль

3. `sudo docker-compose up -d`
4. `pip install -r requirements.txt`
5. `./manage.py migrate`
6. `./manage.py runserver`


Написан swager для быстроты.


