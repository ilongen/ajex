FROM python:3.13-slim

WORKDIR /home/ajex/

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3-dev build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
