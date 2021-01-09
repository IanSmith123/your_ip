FROM python:3.6

LABEL maintainer="Les1ie <me@les1ie.com>"

ADD docker-entrypoint.sh /docker-entrypoint.sh

WORKDIR /app
COPY requirements.txt .
RUN python -m pip install -r requirements.txt -i https://pypi.douban.com/simple
COPY . .
RUN chmod +x ./wait-for-it.sh

#COPY src/ /usr/src/
#ADD docker-entrypoint.sh /docker-entrypoint.sh
#RUN chmod +x /docker-entrypoint.sh

#WORKDIR /usr/src
#ENTRYPOINT [ "/docker-entrypoint.sh"]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]