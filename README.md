# Проект Foodgram

- Имя образа в DockerHub - rakk69/foodgram-backend, rakk69/foodgram-frontend
- Ip сервера - 158.160.67.193

## Автор проекта

- [Артём Хрущёв](https://github.com/TeenCreek)

## Доступен следующий функционал:

- Публикация собственного рецепта
- Подписка на другого автора, чтобы отслеживать его рецепты
- Добавление рецептов в избранное
- Добавление рецептов в корзину, а также возможность скачать список ингредиентов

## Используемые технологии:

- Python
- Django
- DRF
- JWT
- Joser
- Docker
- Gunicorn
- PostgreSQL
- Nginx

## Как запустить проект:

1. Клонировать репозиторий

   ```
   git clone git@github.com:TeenCreek/foodgram-project-react.git
   ```

2. Подключиться на удаленный сервер, установить Docker и Docker-compose:

   ```
   sudo apt install docker.io

   curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

   chmod +x /usr/local/bin/docker-compose
   ```

3. Изменить в файле nginx.conf Ip-адрес

4. Добавить переменные в GitHub Actions:

- SECRET_KEY - секретный ключ Django-проекта из settings.py
- ALLOWED_HOSTS - разрешенный хост сервера
- ENGINE - движок postgresql (django.db.backends.postgresql)
- DB_NAME - имя базы данных
- POSTGRES_USER - логин для подключения к базе данных
- POSTGRES_PASSWORD - пароль для подключения к базе данных
- DB_HOST - название контейнера
- DB_PORT - порт для подключения к базе данных
- HOST - IP сервера
- USER - имя пользователя на сервере
- SSH_KEY - ssh ключ для подключения к серверу
- PASSPHRASE - кодовое слово для подтверждения ssh ключа
- DOCKER_USERNAME - имя пользователя на Dockerhub
- DOCKER_PASSWORD - пароль на Dockerhub
- TELEGRAM_TO - id пользователя в Telegram для уведомления об успешном выполнении проверок GitHub Actions
- TELEGRAM_TOKEN - токен бота в telegram, от которого будет отправляться уведомление

5. Сделать миграции, создать суперпользователя и собрать статику:

   ```
   sudo docker-compose exec backend python manage.py migrate
   sudo docker-compose exec backend python manage.py createsuperuser
   sudo docker-compose exec backend python manage.py collectstatic --no-input
   ```

6. Заполнить базу данными из файла:
   ```
   sudo docker-compose exec backend python manage.py load_database
   ```

> Главная страница сайта: http://158.160.67.193/recipes

> Адрес для работы в админке: http://158.160.67.193/admin

> Подробную документацию по запросам к API можно посмотреть по [ссылке](http://158.160.67.193/api/docs/redoc.html) после запуска сервера с проектом.

![example workflow](https://github.com/TeenCreek/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)
