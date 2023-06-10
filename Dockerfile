FROM python:3.9.7-alpine3.14

EXPOSE 8080

WORKDIR /service

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

CMD [ "python", "service.py" ]