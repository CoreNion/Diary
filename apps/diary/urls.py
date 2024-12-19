from django.urls import path

from . import views

app_name = "diary"

urlpatterns = [
    path('', views.index, name="home"),
    path('entry/create/',views.CreateEntryView.as_view(), name="create"),
    path('entry/<int:pk>', views.UpdateEntryView.as_view(), name="editor")
]