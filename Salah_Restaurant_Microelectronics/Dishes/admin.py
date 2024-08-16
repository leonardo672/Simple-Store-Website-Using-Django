from django.contrib import admin
from .models import Dishes



class DishesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

#class MovieAdmin(admin.ModelAdmin):
   # readonly_fields = ('id',)

admin.site.register(Dishes, DishesAdmin)
#admin.site.register(Movie, MovieAdmin)