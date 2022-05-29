FROM python:3.10.0

WORKDIR /web

RUN pip install -U pip; \
    pip install https://projects.unbit.it/downloads/uwsgi-lts.tar.gz

COPY requirements.txt /requirements.txt
RUN pip install -U pip; pip install -r /requirements.txt