### IMPORT Fixtures

python3.12 manage.py loaddata "{{app_directory }}/fixtures/fixture_{{app_name}}.json.gz";


#### EXPORT Fixtures

python3.12 manage.py dumpdata dashboard --output={{app_directory }}/fixtures/fixture_{{app_name}}.json.gz












### command
alias startapp='my_startapp() { django-admin startapp --extension=py,md --verbosity=3 --template=/home/cosmin/Work/django-startapp-template "$1" && find ./"$1"/templates/"$1" -type f -name "*.html" -exec sed -i "s/<<<app_name>>>/$1/g" {} +; }; my_startapp'
### this are default template file for project, excluded from app. just copy in project root
--exclude=_static 
--exclude=_templates
### introduce modificari in urmnatoarele extensii
--extension=py,md
### cauta si inlocuiete <<<app_name>>> in fisierele html din folderul templates


