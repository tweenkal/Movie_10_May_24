from django.contrib import admin
from .models import category,female_actor,male_actor,movie,multiplex,shows

# Register your models here.

class showcategory(admin.ModelAdmin):
    list_display = ["name","description"]

admin.site.register(category,showcategory)

class showmale_actor(admin.ModelAdmin):
    list_display = ["name","dob","description"]

admin.site.register(male_actor,showmale_actor)

class showfemale_actor(admin.ModelAdmin):
    list_display = ["name","dob","description"]

admin.site.register(female_actor,showfemale_actor)

class showmovie(admin.ModelAdmin):
    list_display = ["name","description","actor","actress","moviecategory"]

admin.site.register(movie,showmovie)

class showmultiplex(admin.ModelAdmin):
    list_display = ["name","address","no_of_screens","city","state","website"]

admin.site.register(multiplex,showmultiplex)

class showshows(admin.ModelAdmin):
    list_display = ["moviename","multiplex","showstime","seats","ticket_price","type","language"]

admin.site.register(shows,showshows)