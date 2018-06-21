FROM python:3.6.5-alpine3.7

RUN apk update && apk add \
    net-tools \
    build-base \
    libxml2-dev \
    libxslt-dev \
    py2-pip \
    ca-certificates \
    musl-dev \
    musl-utils \
    musl-dbg \
    libevent-dev \
    libxml2-dev \ 
    libxslt-dev \
    libffi-dev \
    openssl-dev

RUN pip install --upgrade pip setuptools wheel

# Environment vars
ENV APP_HOME /app
 
# Config app dir
RUN mkdir $APP_HOME
WORKDIR $APP_HOME 
 
# Copy codebase into workdir
COPY . $APP_HOME

RUN pip install -r requirements.txt
RUN ash

CMD ["python", "main.py"]
