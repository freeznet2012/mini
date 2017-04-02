from django.shortcuts import render
from .models import Rrc
# Create your views here.
def index(request):
	list = Rrc.objects.all() 
	return render(request,
        'rrc.html',
        context={'list':list},
    )


def detail(request, rrc_id):
	list = Rrc.objects.filter(id=rrc_id)
	return render(request,
	        'detail.html',
	        context={'list':list},
	    )