from django.db import models
import json

# from django.db.models import JSONField
from django.contrib.postgres.fields import JSONField


# try:
#     from django.db.models import JSONField
# except ImportError:
#     from django.contrib.postgres.fields import JSONField


# Create your models here.

class MyIP(models.Model):
    """
    sample: {"ip":"1.2.3.4", "domain":"example.com"}
    """
    ip = JSONField(verbose_name="addr")
    # ip = models.CharField(max_length=10)

    def __str__(self):
        return json.dumps(self.ip)
