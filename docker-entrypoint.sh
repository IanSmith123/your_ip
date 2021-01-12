#!/bin/bash

set -ex
cd /app

chmod +x wait-for-it.sh
./wait-for-it.sh -t 0 psql:5432 -- echo "postgres is up"

python manage.py makemigrations
python manage.py migrate
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_user('flag', 'flag{djang0_you_are_so_cool}', 'ppiippp') if not User.objects.filter(username='flag').exists() else 0;"

exec "$@"