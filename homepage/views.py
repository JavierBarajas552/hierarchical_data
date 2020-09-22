from django.shortcuts import render
from .models import Folder
# Create your views here.


def index(request):
    folders = Folder.objects.all()
    return render(request, 'index.html', {'folders': folders})
