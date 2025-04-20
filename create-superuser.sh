#!/bin/bash
# Usage: SUPERUSER_NAME=admin SUPERUSER_EMAIL=admin@example.com SUPERUSER_PASSWORD=adminpass ./create-superuser.sh
poetry run python manage.py shell << END
import os
from django.contrib.auth import get_user_model
User = get_user_model()
username = os.environ.get('SUPERUSER_NAME', 'admin')
email = os.environ.get('SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('SUPERUSER_PASSWORD', 'adminpass')
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser {username} created.")
else:
    print(f"Superuser {username} already exists.")
END
