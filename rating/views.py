from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Deputy, UniqueUser
from .helpers import get_usd_rate, user_ip
import requests


@csrf_exempt
def index(request):
    IP = user_ip(request)
    print(IP)
    if request.is_ajax():
        
        pk = int(request.POST['pk'])
        deputy = Deputy.objects.filter(pk=pk).first()
        user = UniqueUser.objects.filter(ip=IP).first()

        if user:
            if deputy.uniqueuser_set.filter(ip=IP).exists():
                print('user exists, and he already voted for this deputy')
            else:
                print('user exists, but he is not voted for this deputy')
        else:
            # u = UniqueUser(ip=IP)
            # u.save()
            print('no user with such ip, create it and count vote for this deputy')

        print(pk)
        response = {
            'status': 'success'
        }
        return JsonResponse(response)
    else:
        context = {}
        context['usd_rate'] = get_usd_rate()
        context['deputies'] = Deputy.objects.order_by('position_current')

        return render(request, 'rating/index.html', context)
   