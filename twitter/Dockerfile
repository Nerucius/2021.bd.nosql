FROM python:3-alpine

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod a+x docker-entrypoint.sh
ENTRYPOINT [ "sh", "-c", "./docker-entrypoint.sh" ]
