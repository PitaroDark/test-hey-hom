#!/bin/bash
. ./.env
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | python manage.py shell
echo "django superuser created"
python3 manage.py runserver 0.0.0.0:${DJANGO_PORT}