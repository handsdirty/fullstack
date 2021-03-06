# coding: utf-8
from datetime import timedelta

# 看起来用RabbitMQ做broker总是出问题，原因不明.
# BROKER_URL = 'amqp://dongwm:123456@localhost:5672/web_develop'
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']

CELERYBEAT_SCHEDULE = {
    'add': {
        'task': 'projb.tasks.add',
        'schedule': timedelta(seconds=10),
        'args': (16, 16)
    }
}
CELERY_SEND_TASK_SENT_EVENT = True
