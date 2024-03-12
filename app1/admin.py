from django.contrib import admin

# Register your models here.
from .models import  Personal,Empleo

admin.site.register(Personal)
admin.site.register(Empleo)