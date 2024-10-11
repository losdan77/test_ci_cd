FROM python:3.10

RUN mkdir /ci_cd_test

WORKDIR /ci_cd_test

COPY requeriments.txt .

RUN pip install -r requeriments.txt

COPY . .

CMD [ "gunicorn", "app:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000" ]