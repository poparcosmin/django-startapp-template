from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy

from .models import {{ app_name|capfirst }}
from .forms import {{app_name|capfirst}}Form

class HomePageView(TemplateView):
    template_name = '{{ app_name }}/{{ app_name }}_home.html'

class {{ app_name|capfirst }}ListView(ListView):
    # Display a list of {{ app_name }} objects
    model = {{ app_name|capfirst }}
    template_name = "= "{{ app_name }}/{{ app_name }}_list.html"

class {{ app_name|capfirst }}DetailView(DetailView):
    # Display details for a single {{ app_name }} object
    model = {{ app_name|capfirst }}
    template_name = "= "{{ app_name }}/{{ app_name }}_detail.html"

    def get(self, request, *args, **kwargs):
        try:
            # Get the object requested and render the template
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        except:
            # Handle case where object does not exist
            return HttpResponseNotFound("Object not found")


class {{ app_name|capfirst }}CreateView(CreateView):
    # Display a form to create a new {{ app_name }} object
    model = {{ app_name|capfirst }}
    form_class = {{app_name|capfirst}}Form # replace with your own form, if desired
    success_url = reverse_lazy("{{ app_name }}_list") # replace with desired URL
    template_name = "= "{{ app_name }}/{{ app_name }}_form.html"

    def form_valid(self, form):
        # Override form_valid to set any additional fields before saving
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class {{ app_name|capfirst }}UpdateView(UpdateView):
    # Display a form to update an existing {{ app_name }} object
    model = {{ app_name|capfirst }}
    fields = ["nume", "creat"]
    template_name = "= "{{ app_name }}/{{ app_name }}_form.html"


class {{ app_name|capfirst }}DeleteView(DeleteView):
    # Display a confirmation page to delete a {{ app_name }} object
    model = {{ app_name|capfirst }}
    template_name = "= "{{ app_name }}/{{ app_name }}_confirm_delete.html"
    success_url = reverse_lazy("{{ app_name }}_list") # replace with desired URL
