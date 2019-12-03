import requests
from django.http import JsonResponse
from ipware import get_client_ip
from .rada.scraper import laws_by_deputy
from .googler.scraper import total_search_results
from .models import Deputy, UniqueUser
import csv


def refresh_deputies_laws_number():
    """Update each deputy's submitted laws"""

    deputies_dict = deputies_law_number()
    sorted_dict = sorted(deputies_dict.items(), key=lambda x: x[1])
    for idx, val in enumerate(sorted_dict): 
        pk = val[0]
        deputy = Deputy.objects.filter(pk=pk).first()
        deputy.submitted_laws = idx + 1
        deputy.save()


def deputies_law_number():
    deputies = Deputy.objects.all()
    places = {}
    for deputy in deputies:
        laws = laws_by_deputy(deputy.rada_id)
        places[deputy.pk] = laws
    return places


def refresh_deputies_google_search_number():
    """Scale deputies google searches from 1 to MAX and update"""

    deputies_dict = deputies_mean_searches()
    sorted_dict = sorted(deputies_dict.items(), key=lambda x: x[1])
    for idx, val in enumerate(sorted_dict): 
        pk = val[0]
        deputy = Deputy.objects.filter(pk=pk).first()
        deputy.monitoring = idx + 1
        deputy.save()
    

def deputies_mean_searches():
    """Return dict - {deputy_pk: mean_num_of_searches, }"""
    deputies = Deputy.objects.all()
    places = {}
    for deputy in deputies:
        rus = int(total_search_results(deputy.surname()))
        ukr = int(total_search_results(deputy.surname_ukr()))
        mean = int((rus + ukr) / 2)
        places[deputy.pk] = mean
    return places


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


def handle_vote(request):
    """TODO: refactor this mess"""
    pk = int(request.POST['pk'])
    deputy = Deputy.objects.filter(pk=pk).first()
    user_IP = user_ip(request)
    user = UniqueUser.objects.filter(ip=user_IP).first()

    if user:
        if deputy.uniqueuser_set.filter(ip=user_IP).exists():
            user.deputies.remove(deputy)
            response = {
                'status': 'removed',
                'amount': deputy.votes()
            }
            return JsonResponse(response)
        else:
            user.deputies.add(deputy)
    else:
        try:
            u = UniqueUser(ip=user_IP)
            u.save()
            u.deputies.add(deputy)
        except IntegrityError:
            response = {
                'status': 'badip',
                'amount': deputy.votes()
            }
            return JsonResponse(response)


    response = {
        'status': 'success',
        'amount': deputy.votes()
    }
    return JsonResponse(response)


def export_csv():
    """"""
    deputies = Deputy.objects.all()
    with open('deputies.csv', mode='w', encoding='utf-8-sig') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        rows = []
        for deputy in deputies:
            place = deputy.position_current
            name = deputy.name
            upr = deputy.upr
            smi = deputy.monitoring
            experts = deputy.experts
            laws = deputy.submitted_laws
            total = deputy.total()
            rows.append([place, name, upr, smi, experts, laws, total])

        sorted_rows = sorted(rows, key = lambda x: int(x[-1]), reverse=True)

        employee_writer.writerow( ['Позиция', 'Имя', 'UPR', 'СМИ', 'ЭКС', 'ЗД', 'Общий'] )
        for row in sorted_rows:
            employee_writer.writerow(row)


def sort_deputies():
    """Change deputies places by total points, 
    save current_positions as last_month_position
    """
    deputies = Deputy.objects.all()
    places = {deputy.pk: deputy.total() for deputy in deputies}

    sorted_dict = sorted(places.items(), key=lambda x: x[1], reverse=True)
    for idx, val in enumerate(sorted_dict): 
        pk = val[0]
        deputy = Deputy.objects.filter(pk=pk).first()
        deputy.last_month_position = deputy.position_current
        deputy.position_current = idx + 1
        deputy.save()


