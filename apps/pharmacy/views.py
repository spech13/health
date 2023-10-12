from django.shortcuts import render
from django.http import HttpResponse

def diseases(request):
    return render(request, "pharmacy/diseases.html")