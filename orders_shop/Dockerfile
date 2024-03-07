# версия python
FROM python:3.12-alpine
ENV PYTHONUNBUFFERED 1
# рабочая директория
WORKDIR /app
# Копируем requirements.txt внутрь контейнера
COPY ../requirements.txt .
# устанавливаем завичимости
RUN pip install --upgrade pip && pip install -r requirements.txt
# копируем проект
COPY .. .
# порт
EXPOSE 8000
# запуск проекта
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# запуск скрипта
#ENTRYPOINT bash.sh

