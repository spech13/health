from django.db import models

class Tablet(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return self.name