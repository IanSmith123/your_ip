#!/bin/bash

set -ex
cd /app

wait-for-it.sh -t 0 psql:5432 -- echo "postgres is up"

python manage.py migrate
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_user('flag', 'flag{wow_you_are_so_cool}', 'ppp')"

exec "$@"