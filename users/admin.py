from django.contrib import admin
from .models import *


# class PersonAdmin(admin.ModelAdmin):
#     fields = ['first_name', 'last_name', 'middle_name', 'password', 'username']
#     search_fields = ['last_name', 'first_name', 'middle_name', 'username']  # фильтр поисковой


admin.site.register(Person)
# admin.site.register(Person, PersonAdmin)