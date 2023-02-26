import pytest
from django.urls import reverse

from ..models import {{ app_name|capfirst }}
from ..views import (
    {{ app_name|capfirst }}ListView, 
    {{ app_name|capfirst }}DetailView, 
    {{ app_name|capfirst }}CreateView, 
    {{ app_name|capfirst }}UpdateView, 
    {{ app_name|capfirst }}DeleteView )

@pytest.fixture
def {{ app_name }}():
    return {{ app_name|capfirst }}.objects.create(nume="test", creat="2022-02-01 12:00:00")

@pytest.fixture
def client():
    return Client()


class Test{{ app_name|capfirst }}Model:
    def test_str_method(self, {{ app_name }}):
        assert str({{ app_name }}) == "test"

    def test_get_absolute_url(self, {{ app_name }}):
        url = reverse("{{ app_name }}:{{ app_name }}", args=[str({{ app_name }}.pk)])
        assert {{ app_name }}.get_absolute_url() == url

    def test_soft_delete(self):
        obj = {{ app_name|capfirst }}.objects.create(nume="test1", creat="2022-02-01 12:00:00", soft_delete=True)
        assert obj in {{ app_name|capfirst }}.objects.all()
        assert obj not in {{ app_name|capfirst }}.visible_objects.all()

    def test_save_method(self, {{ app_name }}):
        {{ app_name }}.soft_delete = True
        {{ app_name }}.save()
        assert {{ app_name }}.soft_delete == False


class Test{{ app_name|capfirst }}ListView:
    def test_view_url_exists_at_desired_location(self):
        url = reverse("{{ app_name }}_list")
        response = self.client.get(url)
        assert response.status_code == 200

    def test_view_url_accessible_by_name(self):
        url = reverse("{{ app_name }}_list")
        response = self.client.get(url)
        assert response.status_code == 200
        assert "object_list" in response.context

    def test_view_uses_correct_template(self):
        url = reverse("{{ app_name }}_list")
        response = self.client.get(url)
        assert response.status_code == 200
        assert "template_name" in response
        assert response.template_name == "{{ app_name }}/{{ app_name }}_list.html"


class Test{{ app_name|capfirst }}DetailView:
    def test_view_url_exists_at_desired_location(self, {{ app_name }}):
        url = reverse("{{ app_name }}_detail", args=[{{ app_name }}.pk])
        response = self.client.get(url)
        assert response.status_code == 200

    def test_view_url_accessible_by_name(self, {{ app_name }}):
        url = reverse("{{ app_name }}_detail", args=[{{ app_name }}.pk])
        response = self.client.get(url)
        assert response.status_code == 200
        assert "object" in response.context

    def test_view_uses_correct_template(self, {{ app_name }}):
        url = reverse("{{ app_name }}_detail", args=[{{ app_name }}.pk])
        response = self.client.get(url)
        assert response.status_code == 200
        assert "template_name" in response
        assert response.template_name == "{{ app_name }}/{{ app_name }}_detail.html"




class Test{{ app_name|capfirst }}CreateView:
    def test_view_url_exists_at_desired_location(self, client):
        url = reverse("{{ app_name }}_create")
        response = client.get(url)
        assert response.status_code == 200

    def test_view_url_accessible_by_name(self, client):
        url = reverse("{{ app_name }}_create")
        response = client.get(url)
        assert response.status_code == 200
        assert "form" in response.context

    def test_view_uses_correct_template(self, client):
        url = reverse("{{ app_name }}_create")
        response = client.get(url)
        assert response.status_code == 200
        assert "template_name" in response
        assert response.template_name == "{{ app_name }}/{{ app_name }}_form.html"

    def test_form_submission(self, client):
        initial_count = {{ app_name|capfirst }}.objects.count()
        data = {
            "nume": "test2",
            "creat": "2022-03-01 12:00:00",
        }
        response = client.post(reverse("{{ app_name }}_create"), data=data)
        assert response.status_code == 302
        assert {{ app_name|capfirst }}.objects.count() == initial_count + 1
