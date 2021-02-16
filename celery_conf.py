from celery.schedules import crontab
from dotenv import load_dotenv
from os import environ as environment_variables

load_dotenv()

imports = ("scripts.task")

beat_schedule = {
    'random_task_runner': {
        'task': 'random_task_runner',
        'schedule': crontab(minute='*/2'), # this is supposed to run everyday at 
    }}
  

CELERY_REDIS_SCHEDULER_URL = environment_variables.get('CELERY_BROKER_URL')
timezone = 'UTC'
redbeat_redis_url = CELERY_REDIS_SCHEDULER_URL
broker_url = CELERY_REDIS_SCHEDULER_URL
result_backend = CELERY_REDIS_SCHEDULER_URL
