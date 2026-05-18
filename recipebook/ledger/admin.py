from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [
        RecipeIngredientInline,
    ]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ("name",)
    search_fields = ("name",)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(admin.BaseUserAdmin):
    inlines = [ProfileInline,]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
