from django.shortcuts import render
from django.http import HttpResponse
from .models import Deputy
from .helpers import get_usd_rate, user_ip
import requests


def index(request):
    context = {}
    context['usd_rate'] = get_usd_rate()
    context['deputies'] = Deputy.objects.order_by('position_current')
    IP = user_ip(request)
    # TODO: create new view for votes, and 
    print(f'User IP: [{IP}]')

    return render(request, 'rating/index.html', context)

# TODO:
# def vote(request):
#     if post:
#         if users_IP not in Voter.objects:
#             deputy_voted_for.votes += 1
#             store users_IP in db
#         else:
#             just fake that user voted
   