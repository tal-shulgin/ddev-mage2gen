FROM python:3.7

WORKDIR /usr/app/src
ARG UNAME=app
ARG UID=1000
ARG GID=1000

RUN groupadd -g $GID -o $UNAME
RUN useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY run_app.sh /run_app.sh
RUN chown -R $UNAME:$UNAME /usr/app/src
RUN chmod +x /run_app.sh
RUN chmod +x /*.sh

CMD ["/run_app.sh"]

EXPOSE 8000