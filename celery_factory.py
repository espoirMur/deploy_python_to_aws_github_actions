from celery import Celery


celery = Celery('tasks_runner', config_source='celery_conf')
