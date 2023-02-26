from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import {{ app_name|capfirst }}

class {{ app_name|capfirst }}ListView(ListView):
    model = {{ app_name|capfirst }}
    template_name = "{{ app_name }}_list.html"

class {{ app_name|capfirst }}DetailView(DetailView):
    model = {{ app_name|capfirst }}
    template_name = "{{ app_name }}_detail.html"

class {{ app_name|capfirst }}CreateView(CreateView):
    #se pastreaza doar una din variantele de mai jos, cu sau fara MyModelForm
    model = {{ app_name|capfirst }}
    form_class = MyModelForm                       # pentru varianta cu form MyModelForm 
    success_url = reverse_lazy("home")     # pentru varianta cu form MyModelForm
    template_name = "{{ app_name }}_form.html"
    # fields = ["nume", "creat"]                     # pentru varianta cu fields / fara MyModelForm 

class {{ app_name|capfirst }}UpdateView(UpdateView):
    model = {{ app_name|capfirst }}
    fields = ["nume", "creat"]
    template_name = "{{ app_name }}_form.html"

class {{ app_name|capfirst }}DeleteView(DeleteView):
    model = {{ app_name|capfirst }}
    template_name = "{{ app_name }}_confirm_delete.html"
    success_url = reverse_lazy("home")
