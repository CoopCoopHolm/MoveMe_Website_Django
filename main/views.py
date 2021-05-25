from django.http import HttpResponse
from django.shortcuts import  render
from .forms import ImageForm

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


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'consignment.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'consignment.html', {'form': form})

def success(request):
    return HttpResponse('successfully uploaded')