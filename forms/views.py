from django.shortcuts import render

# Create your views here.
from .forms import EmailForm
def home(request):
    form = EmailForm()
    context = {"form": form}
    template = "home.html"
    return render(request, template, context)