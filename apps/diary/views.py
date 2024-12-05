from django.shortcuts import render

def index(request):
  if request.user.is_authenticated:
    return render(request, "diary/index_home.html")
  else:
    return render(request, "diary/index_entrance.html")