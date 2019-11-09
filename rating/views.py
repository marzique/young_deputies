from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Deputy, UniqueUser
from .helpers import get_usd_rate, user_ip
import requests


@csrf_exempt
def index(request):
    user_IP = user_ip(request)
    user = UniqueUser.objects.filter(ip=user_IP).first()
    if request.is_ajax():
        pk = int(request.POST['pk'])
        deputy = Deputy.objects.filter(pk=pk).first()

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
            u = UniqueUser(ip=user_IP)
            u.save()
            u.deputies.add(deputy)

        response = {
            'status': 'success',
            'amount': deputy.votes()
        }
        return JsonResponse(response)

    else:
        context = {}
        context['usd_rate'] = get_usd_rate()
        context['deputies'] = Deputy.objects.order_by('position_current')
        if user:
            context['voted'] = [ deputy.pk for deputy in user.deputies.all()]

        return render(request, 'rating/index.html', context)
   