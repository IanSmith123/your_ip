from django.db import models


# Create your models here.

class MyIP(models.Model):
    """
    sample: {"ip":"1.2.3.4", "domain":"example.com"}
    """
    ip = models.JSONField(verbose_name="addr")

    def __str__(self):
        return self.ip
