from django.db import models
from django.conf import settings


class OrderProgress(models.Model):
    is_accepted = models.BooleanField(default=False)
    accepted_at = models.DateTimeField(null=True, blank=True)
    is_being_cooked = models.BooleanField(default=False)
    start_cooking_at = models.DateTimeField(null=True, blank=True)
    is_being_prepared = models.BooleanField(default=False)
    start_preparing_at = models.DateTimeField(null=True, blank=True)
    is_being_delivered = models.BooleanField(default=False)
    start_delivering_at = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
