from django.urls import path
from views import ({{ app_name|capfirst }}ListView, {{ app_name|capfirst }}DetailView, {{ app_name|capfirst }}CreateView, {{ app_name|capfirst }}UpdateView, {{ app_name|capfirst }}DeleteView,)

app_name = "{{ app_name }}"

urlpatterns = [
    path("", {{ app_name|capfirst }}View.as_view(), name="home"),
]
