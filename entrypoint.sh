#!/bin/bash
. ./.env

python3 server/manage.py migrate
python3 server/manage.py makemigrations
python3 server/manage.py migrate

echo "from django.contrib.auth import get_user_model; 
User = get_user_model(); 
User.objects.create_superuser('admin', 'admin@example.com', 'admin')
" | python server/manage.py shell
echo "django superuser created"
python3 server/manage.py runserver 0.0.0.0:${DJANGO_PORT}