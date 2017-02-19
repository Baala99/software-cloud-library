from django.db import models


class Software(models.Model):
    name = models.CharField(max_length=64)
    file = models.FileField(upload_to='uploads/')

    class Meta:
        verbose_name_plural = "software"

    def __str__(self):
        return self.name
