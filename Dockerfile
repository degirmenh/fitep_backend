FROM python:3

ENV PYTHONUNBUFFERED 1

RUN make /code
WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--chdir", "fitep_backend", "--bind", ':8000', 'fitep:wsgi:application']