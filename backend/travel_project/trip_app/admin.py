from django.contrib import admin
from .models import Post, Trips

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "create")
    list_display = ("title", "create", "author_id", "rating")


@admin.register(Trips)
class TripsAdmin(admin.ModelAdmin):
    search_fields = ("user_id", "location")
    list_display = ("user_id", "location", "start_date")
