from django.contrib import admin

# Register your models here.
from TemitopePortfolioApp.models import Cat, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username",)


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ("name", "photo")
