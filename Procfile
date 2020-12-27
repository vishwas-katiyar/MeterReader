release: python manage.py migrate
web: gunicorn MeterReader.wsgi:application --log-file - --log-level debug
