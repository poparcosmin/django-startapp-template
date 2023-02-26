import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User

from ..models import {{app_name|capfirst}}
from ..views import {{app_name|capfirst}}ListView, {{app_name|capfirst}}CreateView, {{app_name|capfirst}}UpdateView
from ..forms import {{app_name|capfirst}}Form


@pytest.fixture
def user():
    return User.objects.create_user(
        username="testuser",
        email="testuser@example.com",
        password="testpass"
    )


@pytest.fixture
def {{app_name}}():
    return {{app_name|capfirst}}.objects.create(nume="test", creat="2022-02-01 12:00:00")


@pytest.fixture
def client():
    return Client()


class Test{{app_name|capfirst}}ListView:

    def test_{{app_name}}_list_view(self, client, {{app_name}}):
        response = client.get(reverse("{{app_name}}_list"))
        assert response.status_code == 200
        assert {{app_name|capfirst}}.objects.count() == 1
        assert response.context_data["object_list"].count() == 1
        assert response.context_data["object_list"][0] == {{app_name}}

    def test_{{app_name}}_list_view_pagination(self, client, {{app_name}}):
        # Create 10 {{app_name}} objects
        for i in range(10):
            {{app_name|capfirst}}.objects.create(nume=f"test{i}", creat="2022-02-01 12:00:00")
        response = client.get(reverse("{{app_name}}_list"))
        assert response.status_code == 200
        assert {{app_name|capfirst}}.objects.count() == 11
        assert response.context_data["paginator"].count == 11
        assert len(response.context_data["page_obj"]) == 10


class Test{{app_name|capfirst}}CreateView:

    def test_{{app_name}}_create_view(self, client, user):
        client.login(username="testuser", password="testpass")
        response = client.get(reverse("{{app_name}}_create"))
        assert response.status_code == 200
        assert isinstance(response.context_data["view"], {{app_name|capfirst}}CreateView)

    def test_{{app_name}}_create_view_post(self, client, user):
        client.login(username="testuser", password="testpass")
        form_data = {"nume": "test2", "creat": "2022-03-01 12:00:00"}
        response = client.post(reverse("{{app_name}}_create"), data=form_data)
        assert response.status_code == 302
        assert {{app_name|capfirst}}.objects.count() == 1


class Test{{app_name|capfirst}}UpdateView:

    def test_{{app_name}}_update_view(self, client, user, {{app_name}}):
        client.login(username="testuser", password="testpass")
        response = client.get(reverse("{{app_name}}_update", kwargs={"pk": {{app_name}}.pk}))
        assert response.status_code == 200
        assert isinstance(response.context_data["view"], {{app_name|capfirst}}UpdateView)

    def test_{{app_name}}_update_view_post(self, client, user, {{app_name}}):
        client.login(username="testuser
