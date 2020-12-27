release: python manage.py migrate
clock: python cron.py
web: gunicorn MeterReader.wsgi:application --log-file - --log-level debug
