FROM python:3.9-slim

WORKDIR /usr/app/src

COPY . /usr/app/src

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver_plus", "0.0.0.0:8000"]