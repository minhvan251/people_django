from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, redirect
# Create your views here.

def home(request):
    return render(request,'structure/home.html')
def about(request):
    return render(request,'structure/about.html')
