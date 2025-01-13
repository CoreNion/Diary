from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from .models import EntryModel

def index(request):
  if request.user.is_authenticated:
    entry_list = EntryModel.objects.all()
    return render(request, "diary/index_home.html", {'entry_list': entry_list})
  else:
    return render(request, "diary/index_entrance.html")
  
class CreateEntryView(LoginRequiredMixin, CreateView):
  template_name = "diary/editor.html"
  model = EntryModel
  fields = {"title", "content", "tags", "date", "time"}
  success_url = reverse_lazy("diary:home")

class UpdateEntryView(LoginRequiredMixin, UpdateView):
  template_name = "diary/editor.html"
  model = EntryModel
  fields = {"title", "content", "tags", "date", "time"}
  success_url = reverse_lazy("diary:home")

  def get_object(self, queryset=None):
    obj: EntryModel = super().get_object(queryset)
    obj.date = obj.date.strftime("%Y-%m-%d")
    obj.time = obj.time.strftime("%H:%M")

    return obj