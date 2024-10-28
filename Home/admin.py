from django.contrib import admin
from .models import robo

# Register your models here.

class roboAdmin(admin.ModelAdmin):
  list_display = ("username", "like", "comment","share","post","about")
  
admin.site.register(robo, roboAdmin)