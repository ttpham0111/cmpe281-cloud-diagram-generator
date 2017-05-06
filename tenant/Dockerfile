FROM openjdk:alpine

MAINTAINER Tuan Pham <ttpham0111@gmail.com>

# Install packages
RUN apk add --no-cache wget \
                       make \
                       ca-certificates \
                       musl-dev \
                       gcc \
                       g++ \
                       libffi-dev \
                       python-dev==2.7.13-r0 \
                       graphviz==2.38.0-r6 \
                       ttf-dejavu \
                       fontconfig==2.12.1-r0 && \

    update-ca-certificates && \

    wget "https://bootstrap.pypa.io/get-pip.py" && \
    python get-pip.py && \
    rm -f get-pip.py

RUN wget -O- https://mirrors.kernel.org/gnu/plotutils/plotutils-2.6.tar.gz | tar -xz -C /tmp && \
    cd /tmp/plotutils-2.6 && \
    ./configure && \
    make install && \
    make installcheck && \
    cd pic2plot && \
    make install && \
    cd - && \
    rm -rf /tmp/plotutils-2.6

# Install gunicorn
RUN pip install gunicorn

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
             run_server:app