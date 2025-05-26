FROM python:3.13

WORKDIR /home/ajex/

RUN apt-get update && apt upgrade -y && apt install -y python3-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
