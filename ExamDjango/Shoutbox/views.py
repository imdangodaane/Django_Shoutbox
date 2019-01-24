from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
import pytz

from .models import Shout

# Create your views here.
def index(request):
    return render(request, 'Shoutbox/index.html')

def submit(request):
    name = request.POST.get('name', None)
    text = request.POST.get('text', None)
    s = Shout(shout_name=name, shout_text=text, shout_date=timezone.localtime())
    print(s.shout_date)
    s.save()
    return HttpResponseRedirect(reverse('Shoutbox:result'))


def result(request):
    output = []
    latest_shout_list = Shout.objects.order_by('-shout_date')
    for obj in latest_shout_list:
        date = timezone.localtime(obj.shout_date)
        output.append(': '.join(['-'.join([date.strftime('(%Y/%m/%d %H:%M:%S)'),
                                           obj.shout_name]),
                                obj.shout_text]))
    template = loader.get_template('Shoutbox/result.html')
    context = {
        'output': output,
    }
    return HttpResponse(template.render(context, request))
