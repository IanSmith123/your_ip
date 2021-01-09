FROM python:3.5

LABEL maintainer="Les1ie <me@les1ie.com>"

ADD requ
COPY src/ /usr/src/
ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

WORKDIR /usr/src
ENTRYPOINT [ "/docker-entrypoint.sh"]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]