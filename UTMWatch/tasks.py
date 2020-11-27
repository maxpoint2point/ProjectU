from ProjectU.celery import app
from .service import exchange as ex


@app.task
def exchange(host, port):
    ex.main_exchange(host, port)
