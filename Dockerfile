FROM python:3.11.4-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD bash -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"


