FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt && rm -rf /root/.cache/pip

COPY . /app/

EXPOSE 8282

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8282"]