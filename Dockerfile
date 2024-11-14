# Базовый образ
FROM python:3.10-slim

# Установка рабочей директории
WORKDIR /app

# Копирование скрипта в контейнер
COPY app.py .

# Установка точки входа
ENTRYPOINT ["python", "app.py"]
