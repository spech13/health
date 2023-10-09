from django.db import models


class MedicineForm(models.Model):
    LIQUID = "LIQUID"
    SOLIDE = "SOLIDE"
    MAGIC = "MAGIC"
    AEROSOL = "AEROSOL"

    name = models.CharField(
        verbose_name="Name",
        max_length=255,
        choices=[
            (LIQUID, "Liquid"),
            (SOLIDE, "Solide"),
            (MAGIC, "Magic"),
            (AEROSOL, "Aerosol"),
        ],
    )

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return self.name


class MedicineType(models.Model):
    DROPS = "DROPS"
    TINCTURE = "TINCTURE"
    INFUSION = "INFUSION"
    SYRUP = "SYRUP"
    SUSPENSION = "SUSPENSION"
    EMULSION = "EMULSION"
    CAPSULE = "CAPSULE"
    TABLET = "TABLET"
    POWDER = "POWDER"
    GRANULE = "GRANULE"
    DRAGEE = "DRAGEE"
    CARAMEL = "CARAMEL"
    PENCIL = "PENCIL"
    CREAM = "CREAM"
    OINTMENT = "OINTMENT"
    GEL = "GEL"
    SUPPOSITORS = "SUPPOSITORS"
    PASTE = "PASTE"

    name = models.CharField(
        verbose_name="Name",
        max_length=255,
        choices=[
            (DROPS, "Drops"),
            (TINCTURE, "Tincture"),
            (INFUSION, "Infusion"),
            (SYRUP, "Syrup"),
            (SUSPENSION, "Suspension"),
            (EMULSION, "Emulsion"),
            (CAPSULE, "Capsule"),
            (TABLET, "Tablet"),
            (POWDER, "Powder"),
            (GRANULE, "Granule"),
            (DRAGEE, "Dragee"),
            (CARAMEL, "Caramel"),
            (PENCIL, "Pencil"),
            (CREAM, "Cream"),
            (OINTMENT, "Ointment"),
            (GEL, "Get"),
            (SUPPOSITORS, "Supppositors"),
            (PASTE, "Paste"),
        ],
    )
    medicine_form = models.ForeignKey(
        MedicineForm, verbose_name="Medicine form", on_delete=models.SET_NULL, null=True
    )

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def get_medicine_form_name(self):
        return self.medicine_form

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)
    description = models.TextField(verbose_name="Description", null=True, blank=True)

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return self.name


class Contraindication(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)
    description = models.TextField(verbose_name="Description", null=True, blank=True)

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)
    medicine_type = models.ForeignKey(
        MedicineType, verbose_name="Medicine type", on_delete=models.SET_NULL, null=True
    )
    disease = models.ManyToManyField(Disease, verbose_name="Diseases")
    contraindication = models.ManyToManyField(
        Contraindication, verbose_name="Contrandications", null=True, blank=True
    )

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return self.name
