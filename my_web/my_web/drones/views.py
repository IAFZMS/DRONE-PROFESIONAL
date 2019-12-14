from django.shortcuts import render  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse 
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
import datetime 
from .models import Dron


def dron_listing(request):
	drones= Dron.objects.all()
	context = {
		'drones': drones
	}
	return render(request, 'drones/index.html', context)
