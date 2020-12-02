from ProjectU.celery import app
from .service import exchange as ex


@app.task
def exchange(workplace):
    ex.main_exchange(workplace)
