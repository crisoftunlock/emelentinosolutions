from django.shortcuts import render
from apps.welcome.models import Welcome

# Create your views here.
def home(request):
    welcome = Welcome.objects.all()
    return render(request, "core/body.html", {'welcome':welcome})