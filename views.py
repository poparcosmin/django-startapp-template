from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView

from .models import {{ app_name|capfirst }}
from .forms import {{app_name|capfirst}}Form

class {{ app_name|capfirst }}View(TemplateView):
    template_name = '{{ app_name }}/home.html'

class {{ app_name|capfirst }}ListView(ListView):
    # Display a list of {{ app_name }} objects
    model = {{ app_name|capfirst }}
    template_name = "{{ app_name }}/list.html"

class {{ app_name|capfirst }}DetailView(DetailView):
    # Display details for a single {{ app_name }} object
    model = Adresa
    template_name = "{{ app_name }}/detail.html"

    def get(self, request, *args, **kwargs):
        try:
            # Get the object requested and render the template
            self.object = self.get_object()
        except {{ app_name|capfirst }}.DoesNotExist:
            # Handle case where object does not exist
            raise Http404("{{ app_name|capfirst }} not found")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)    


class {{ app_name|capfirst }}CreateView(CreateView):
    # Display a form to create a new {{ app_name }} object
    model = {{ app_name|capfirst }}
    form_class = {{app_name|capfirst}}Form # replace with your own form, if desired
    success_url = reverse_lazy("create") # replace with desired URL
    template_name = "{{ app_name }}/form.html"

   def form_valid(self, form):
        # Set additional fields before saving
        adresa = form.save(commit=False)
        adresa.created_by = self.request.user
        adresa.save()
        return super().form_valid(form)


class {{ app_name|capfirst }}UpdateView(UpdateView):
    # Display a form to update an existing {{ app_name }} object
    model = {{ app_name|capfirst }}
    fields = ["nume", "creat"]
    template_name = "{{ app_name }}/form.html"


class {{ app_name|capfirst }}DeleteView(DeleteView):
    # Display a confirmation page to delete a {{ app_name }} object
    model = {{ app_name|capfirst }}
    template_name = "{{ app_name }}/confirm_delete.html"
    success_url = reverse_lazy("list") # replace with desired URL
