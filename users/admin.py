from django.contrib import admin
from users.models import Profile
# Register your models here.

#admin.site.register(Profile)
#Decorador
@admin.register(Profile)
class ProfileAdd(admin.ModelAdmin):
    list_display = ('pk','user','phone_number','website','profile_picture') #Orden columnas en admin
    list_display_links = ('pk','user','phone_number') #columnas likeables
    list_editable = ('website','profile_picture') #campos editables desde la grilla
    search_fields = ('user__email','user__first_name') #Create filters
