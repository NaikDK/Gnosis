from django.shortcuts import render
from .models import Destinations
import datetime

# Create your views here.
def index(request):
    dest = Destinations()
    dest.id = "1"
    dest.img = "1.jpg"
    dest.time = datetime.datetime.now()
    dest.title = "Deep Naik"
    dest.comment = "Test Run"
    dest.description = "This is first Django app so try as much as you can and stpo giving accuses. Happy coding!!"

    return render(request, "index.html", {'dest': dest})