from django.contrib import admin
from .models import Post, Trips

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("place_name", "create")
    list_display = ("place_name", "create", "author_id")


@admin.register(Trips)
class TripsAdmin(admin.ModelAdmin):
    search_fields = ("user_id", "location")
    list_display = ("user_id", "location", "start_date")
