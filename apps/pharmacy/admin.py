from django.contrib import admin
from apps.pharmacy.models import (
    MedicineForm,
    MedicineType,
    Disease,
    Contraindication,
    Medicine,
)


@admin.register(MedicineForm)
class MedicineFormAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")


@admin.register(MedicineType)
class MedicineTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "medicine_form", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Contraindication)
class ContraindicationAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ("name", "medicine_type")
    readonly_fields = ("created_at", "updated_at")
