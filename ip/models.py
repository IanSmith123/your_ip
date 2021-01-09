from django.db import models

try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField


# Create your models here.

class MyIP(models.Model):
    """
    sample: {"ip":"1.2.3.4", "domain":"example.com"}
    """
    ip = JSONField(verbose_name="addr")

    def __str__(self):
        return self.ip
