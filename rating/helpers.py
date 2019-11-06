from ipware import get_client_ip
import requests


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