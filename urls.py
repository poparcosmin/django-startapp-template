from django.urls import path
from .views import (
    {{ app_name|capfirst }}HomeView,
    {{ app_name|capfirst }}ListView,
    {{ app_name|capfirst }}DetailView,
    {{ app_name|capfirst }}CreateView,
    {{ app_name|capfirst }}UpdateView,
    {{ app_name|capfirst }}DeleteView,
)

app_name = "{{ app_name }}"

urlpatterns = [
    path('', {{ app_name|capfirst }}HomeView.as_view(), name='home'),
    path("lista/", {{ app_name|capfirst }}ListView.as_view(), name="list"),
    path("<int:pk>/", {{ app_name|capfirst }}DetailView.as_view(), name="detail"),
    path("creeaza/", {{ app_name|capfirst }}CreateView.as_view(), name="create"),
    path("<int:pk>/update/", {{ app_name|capfirst }}UpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", {{ app_name|capfirst }}DeleteView.as_view(), name="delete"),
]
