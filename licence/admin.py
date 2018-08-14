from django.contrib import admin
from .models import Composition, Licence, ItemComposition

# Register your models here.
class ItemInline(admin.TabularInline):
    model = ItemComposition
    extra = 1

@admin.register(Licence)
class LicenceAdmin(admin.ModelAdmin):
    pass

@admin.register(Composition)
class CompositionAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
