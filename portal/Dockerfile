FROM alpine

MAINTAINER Tuan Pham <ttpham0111@gmail.com>

# Install python and pip
RUN apk add --no-cache curl \
                       musl-dev \
                       gcc \
                       libffi-dev \
                       python-dev==2.7.13-r0 && \
    curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && \
    python get-pip.py && \
    rm -f get-pip.py

# Install gunicorn and gevent
RUN pip install gunicorn \
                gevent==1.2.1

# Install requires first for better caching
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Install app
COPY . /app
RUN pip install /app

# Run app
CMD gunicorn --bind=0.0.0.0:5000 \
             --access-logfile=- \
             --access-logformat="%(t)s %(r)s %(s)s" \
             --workers=1 \
             --worker-class='gevent' \
             run_server:app