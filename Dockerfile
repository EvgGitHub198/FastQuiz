FROM python:3.9

WORKDIR /code

COPY ./req.txt /code/req.txt

RUN pip install -r req.txt

COPY ./app /code/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]