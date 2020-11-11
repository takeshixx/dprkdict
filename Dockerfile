FROM python:alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /srv/dprkdict
WORKDIR /srv/dprkdict/
ADD requirements.txt \
    dprkdict \
    engkor \
    manage.py \
    eng_kor_deobfuscated.dic.sqlite3 \
    /srv/dprkdict/
RUN pip3 install -r requirements.txt
