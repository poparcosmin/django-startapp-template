### IMPORT Fixtures

python3.12 manage.py loaddata "{{app_directory }}/fixtures/fixture_{{app_name}}.json.gz";


#### EXPORT Fixtures

python3.12 manage.py dumpdata dashboard --output={{app_directory }}/fixtures/fixture_{{app_name}}.json.gz












### command
python3.12 manage.py startapp --exclude=_static --exclude=_templates --extension=py,md --verbosity=3 --template=https://github.com/poparcosmin/django-startapp-template/archive/master.zip
### this are default template file for project, excluded from app. just copy in project root
--exclude=_static 
--exclude=_templates
### introduce modificari in urmnatoarele extensii
--extension=py,md
