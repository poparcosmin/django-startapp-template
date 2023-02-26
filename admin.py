from django.contrib import admin
from .models import {{app_name|capfirst}}

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
# 	list_display = ['',]
# 	list_filter = ('',)
# 	list_editable = ('',)
# 	prepopulated_fields = {'slug': ('name',)}

admin.site.register({{app_name|capfirst}})
