from django.shortcuts import render
from .models import Rrc
# Create your views here.
def rrc(request):
	list = Rrc.objects.all() 
	return render(request,
        'rrc.html',
        context={'list':list},
    )