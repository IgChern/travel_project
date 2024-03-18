from django.contrib import admin
from .models import Rating, Comment


# Register your models here.
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    search_fields = ("post", "user", "value")
    list_display = ("post", "user", "value")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ("post", "author", "time_create")
    list_display = ("post", "author", "time_create")
