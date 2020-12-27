release: python manage.py migrate , python manage.py crontab add
web: gunicorn MeterReader.wsgi:application --log-file - --log-level debug
