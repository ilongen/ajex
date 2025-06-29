FROM python:3.13

RUN mkdir /ajex

WORKDIR /ajex

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt /ajex/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /ajex/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
