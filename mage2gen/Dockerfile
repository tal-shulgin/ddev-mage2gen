FROM python:3.9-slim

WORKDIR /usr/app/src

COPY . /usr/app/src

# Create and activate venv in Docker build to avoid issues with pip install
RUN python -m venv /usr/app/venv
RUN /usr/app/venv/bin/pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["/usr/app/venv/bin/python", "manage.py", "runserver_plus", "0.0.0.0:8000"]