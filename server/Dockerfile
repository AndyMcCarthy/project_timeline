#docker run -p "127.0.0.1:8080:8080" -d server
FROM python:3.11-alpine
WORKDIR /server
COPY requirements.txt requirements.txt
RUN apk update
RUN apk add --no-cache \
    build-base \
    freetds-dev \
    g++ \
    gcc \
    tar \
    gfortran \
    gnupg \
    libffi-dev \
    libpng-dev \
    libsasl \
    openblas-dev \
    openssl-dev \
    musl-dev \
    linux-headers
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
WORKDIR /server
COPY . /server
CMD ["python3", "server.py"]