FROM python:3.6

LABEL maintainer="Les1ie <me@les1ie.com>"
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install -r requirements.txt -i https://pypi.douban.com/simple
COPY . .
ADD docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT [ "/docker-entrypoint.sh"]