from django.db import models
from django.utils import timezone


class OrderProgress(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('accepted', 'Accepted'),
        ('being_cooked', 'Being Cooked'),
        ('being_prepared', 'Being Prepared'),
        ('being_delivered', 'Being Delivered'),
        ('completed', 'Completed'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    new_at = models.DateTimeField(null=True, blank=True)
    accepted_at = models.DateTimeField(null=True, blank=True)
    start_cooking_at = models.DateTimeField(null=True, blank=True)
    start_preparing_at = models.DateTimeField(null=True, blank=True)
    start_delivering_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            if self.status == 'new':
                self.new_at = timezone.now()
            elif self.status == 'accepted':
                self.accepted_at = timezone.now()
            elif self.status == 'being_cooked':
                self.start_cooking_at = timezone.now()
            elif self.status == 'being_prepared':
                self.start_preparing_at = timezone.now()
            elif self.status == 'being_delivered':
                self.start_delivering_at = timezone.now()
            elif self.status == 'completed':
                self.completed_at = timezone.now()
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"OrderProgress - {self.get_status_display()}"
