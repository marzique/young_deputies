from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
from .models import Deputy, UniqueUser
from .helpers import get_usd_rate, user_ip, handle_vote
import requests


@csrf_exempt
def index(request):
    if request.is_ajax():
        return handle_vote(request)

    else:
        context = {}
        context['usd_rate'] = get_usd_rate()
        context['deputies'] = Deputy.objects.order_by('position_current')
        
        user = UniqueUser.objects.filter(ip=user_ip(request)).first()
        if user:
            context['voted'] = [ deputy.pk for deputy in user.deputies.all()]

        return render(request, 'rating/index.html', context)
   