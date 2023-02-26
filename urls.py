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
    path('', {{ app_name|capfirst }}HomeView.as_view(), name='{{ app_name }}_home'),
    path("list/", {{ app_name|capfirst }}ListView.as_view(), name="{{ app_name }}_list"),
    path("<int:pk>/", {{ app_name|capfirst }}DetailView.as_view(), name="{{ app_name }}_detail"),
    path("create/", {{ app_name|capfirst }}CreateView.as_view(), name="{{ app_name }}_create"),
    path("<int:pk>/update/", {{ app_name|capfirst }}UpdateView.as_view(), name="{{ app_name }}_update"),
    path("<int:pk>/delete/", {{ app_name|capfirst }}DeleteView.as_view(), name="{{ app_name }}_delete"),
]
