import pytest
from django.urls import reverse

from ..models import {{ app_name|capfirst }}


@pytest.fixture
def {{ app_name }}():
    return {{ app_name|capfirst }}.objects.create(nume="test", creat="2022-02-01 12:00:00")


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
