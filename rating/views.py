from django.shortcuts import render
from django.http import HttpResponse
from .models import Deputy
import requests


def index(request):
    context = {}
    rate = get_usd_rate()
    context['usd_rate'] = rate
    qs = Deputy.objects.order_by('position_current')
    context['deputies'] = qs

    return render(request, 'rating/index.html', context)


# TODO: move it somewhere
def get_usd_rate():
    """Return current USD to UAH rate as float with 2 deciamals after dot"""
    context = {}
    nbu_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

    try: 
        response = requests.get(url=nbu_url)
        data = response.json()
        for item in data:
            if item['cc'] == 'USD':
                return round(item['rate'], 2)
        else:
            return None
    except:
        # if mistake occured 
        # TODO: use explicit excepion here
        get_usd_rate()

# TODO:
# every last day of the month update via CRON like feature:
# - laws number
# - google articles number
