from django.contrib import admin
from .models import Rating


# Register your models here.
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    search_fields = ("post", "user", "value")
    list_display = ("post", "user", "value")
