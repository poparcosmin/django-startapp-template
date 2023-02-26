from django.contrib import admin
from .models import {{app_name|capfirst}}

# @admin.register({{app_name|capfirst}})
# class {{app_name|capfirst}}Admin(admin.ModelAdmin):
# 	list_display = ['',]
# 	list_filter = ('',)
# 	list_editable = ('',)
# 	prepopulated_fields = {'slug': ('name',)}

# admin.site.register({{app_name|capfirst}}, {{app_name|capfirst}}Admin)

admin.site.register({{app_name|capfirst}})
