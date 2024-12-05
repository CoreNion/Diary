from django.shortcuts import render
from .models import EntryModel

def index(request):
  if request.user.is_authenticated:
    entry_list = EntryModel.objects.all()
    return render(request, "diary/index_home.html", {'entry_list': entry_list})
  else:
    return render(request, "diary/index_entrance.html")