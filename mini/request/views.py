from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RequestCreationForm
from .models import Request
from datetime import datetime, timedelta

# Create your views here.

def request(request):
	last_month = datetime.today() - timedelta(days=1)
	list = Request.objects.filter(date_of_request__date__gte=last_month).order_by('date_of_request')
	return render(
        request,
        'request.html',
        context={'list':list},
    )

def create(request):
	if request.method == 'POST':
		form = RequestCreationForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/request')                      
			
		else:
			return HttpResponse('INCORRECT')
	else:
		form = RequestCreationForm()
		
		return render(request,
	        'reg_form.html',
	        context={'form':form}
	    )
