import requests
from ipware import get_client_ip
from .rada.scraper import laws_by_deputy
from .googler.scraper import total_search_results
from .models import Deputy


def refresh_deputies_laws_number():
    """Refresh each deputy's submitted laws"""
    deputies = Deputy.objects.all()
    for deputy in deputies:
        deputy.submitted_laws = laws_by_deputy(deputy.rada_id)
        deputy.save()


def refresh_deputies_google_search_number():
    """Refresh each deputy's google search number"""
    deputies = Deputy.objects.all()
    for deputy in deputies:
        deputy.monitoring = total_search_results(deputy.name_surname())
        deputy.save()


def user_ip(request):
    """Return users IP if possible"""
    client_ip, _ = get_client_ip(request)
    if client_ip is None:
        return None
    else:
        return client_ip


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