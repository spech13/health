from django.contrib import admin
from apps.pharmacy.models import Tablet

@admin.register(Tablet)
class TabletAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")