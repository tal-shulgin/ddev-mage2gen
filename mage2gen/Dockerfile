FROM python:3.9-slim

WORKDIR /usr/src/app

ARG UNAME=app
ARG UID=1000
ARG GID=1000
RUN groupadd -g $GID -o $UNAME
RUN useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME

# Install Git and PostgreSQL development headers
RUN apt-get update && apt-get install -y git libpq-dev

# Create and activate venv in Docker build to avoid issues with pip install
RUN python -m venv /usr/app/venv

RUN git clone https://github.com/tal-shulgin/Mage2Gen-Frontend.git .
RUN git clone -b magento-2.3 https://github.com/Mage2Gen/Mage2Gen.git mage2gen-core/magento2.3
RUN git clone -b magento-2.4 https://github.com/Mage2Gen/Mage2Gen.git mage2gen-core/magento2.4

RUN ln -s ./mage2gen-core/magento2.3/mage2gen ./mage2gen3
RUN ln -s ./mage2gen-core/magento2.4/mage2gen ./mage2gen4

RUN /usr/app/venv/bin/pip install --no-cache-dir -r requirements.txt

RUN python3 manage.py migrate --noinput
RUN python3 manage.py createcachetable

EXPOSE 8000

CMD ["/usr/app/venv/bin/python", "manage.py", "runserver_plus", "0.0.0.0:8000"]