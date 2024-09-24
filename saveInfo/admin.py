from django.contrib import admin

# Register your models here.
from saveInfo.models import SaveInfo
class SaveInfoAdmin(admin.ModelAdmin):
    list_display=('First_Name','Last_Name','Email','Password')
    
admin.site.register(SaveInfo,SaveInfoAdmin)    
