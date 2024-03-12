from django.contrib import admin

# Register your models here.
from .models import  Personal,Empleo


class AdminPersonal(admin.ModelAdmin):
    list_display = ["id","nombre","apellido","edad"]
    list_filter = ["nombre"]

class AdminEmpleo(admin.ModelAdmin):
    list_display = ["id","nombre","experiencia" ,"persona_empleo"]

admin.site.register(Personal ,AdminPersonal)
admin.site.register(Empleo, AdminEmpleo)
