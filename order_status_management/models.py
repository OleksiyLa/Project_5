from django.db import models
from django.conf import settings
from checkout.models import Order


class OrderProgress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    managed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
