![workflow](https://github.com/Suhanov-Mihail/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## workflow

- Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) и запуск pytest. Дальнейшие шаги выполнятся только если push был в ветку master или main.
- build_and_push_to_docker_hub - Сборка и доставка докер-образов на Docker Hub
- deploy - Автоматический деплой проекта на боевой сервер. Выполняется копирование файлов из репозитория на сервер
- send_message - Отправка уведомления в Telegram

# Подготовка для запуска workfklow

Отредактируйте файл `nginx/default.conf` и в строке `server_name` впишите IP виртуальной машины (сервера).  
Скопируйте подготовленные файлы `docker-compose.yaml` и `nginx/default.conf` из вашего проекта на сервер:

```
scp docker-compose.yaml <username>@<host>/home/<username>/docker-compose.yaml
sudo mkdir nginx
scp default.conf <username>@<host>/home/<username>/nginx/default.conf
```
В репозитории на Гитхабе добавьте данные в `Settings - Secrets - Actions secrets`:
```
DOCKER_USERNAME - имя пользователя в DockerHub
DOCKER_PASSWORD - пароль пользователя в DockerHub
HOST - ip-адрес сервера
USER - пользователь
SSH_KEY - приватный ssh-ключ (публичный должен быть на сервере)
PASSPHRASE - кодовая фраза для ssh-ключа
DB_ENGINE - django.db.backends.postgresql
DB_NAME - postgres 
POSTGRES_USER - postgres 
POSTGRES_PASSWORD - postgres 
DB_HOST - db
DB_PORT - 5432
TELEGRAM_TO - id своего телеграм-аккаунта
TELEGRAM_TOKEN - токен бота
```

При команде 'git push' запускается набор блоков команд jobs (см. файл yamdb_workflow.yaml)

