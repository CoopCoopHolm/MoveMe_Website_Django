from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home.html')

def consent(request):
    return render(request, 'consent.html')

def moving(request):
    return render(request, 'moving.html')

def junk_removal(request):
    return render(request, 'junk_removal.html')

def consignment(request):
    return render(request, 'consignment.html')