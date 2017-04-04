from django.db import models


class CreatedModifiedMixin(models.Model):
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True