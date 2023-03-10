### IMPORT Fixtures

python3.12 manage.py loaddata "{{app_directory }}/fixtures/fixture_{{app_name}}.json.gz";


#### EXPORT Fixtures

python3.12 manage.py dumpdata dashboard --output={{app_directory }}/fixtures/fixture_{{app_name}}.json.gz












### command
my_startapp() {
    django-admin startapp --exclude=_static --exclude=_templates --extension=py,md --verbosity=3 --template=https://github.com/poparcosmin/django-startapp-template/archive/master.zip $1 &&
    find ./$1/templates/$1 -type f -name "*.html" -exec sed -i "s/<<<app_name>>>/$1/g" {} +;
}
alias pms='my_startapp'
### this are default template file for project, excluded from app. just copy in project root
--exclude=_static 
--exclude=_templates
### introduce modificari in urmnatoarele extensii
--extension=py,md

