from ProjectU.celery import app
from .models import Workplace
from .service import exchange as ex
from .models import RestHeader


@app.task
def exchange(**kwargs):
    workplace = Workplace.objects.get(pk=kwargs['workplace_id'])
    ex.main_exchange(workplace)


#
# @app.task
# def all_exchange():
#     workplaces = Workplace.objects.filter(disabled=False)
#     for workplace in workplaces:
#         ex.main_exchange(workplace)
#
#
@app.task
def request_rest(**kwargs):
    for workplace in Workplace.objects.filter(pk=kwargs['workplace_id'], disabled=False, request_rest=True):
        r1 = RestHeader(workplace=workplace, type=RestHeader.STOCK)
        r2 = RestHeader(workplace=workplace, type=RestHeader.SHOP)
        r1.save()
        r2.save()
