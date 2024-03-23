from django.contrib import admin
from .models import CommentRating, Comment


# Register your models here.
@admin.register(CommentRating)
class RatingAdmin(admin.ModelAdmin):
    search_fields = ("post", "author", "value")
    list_display = ("post", "author", "value")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ("post", "author", "time_create")
    list_display = ("post", "author", "time_create")
