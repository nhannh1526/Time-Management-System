import numpy as np
# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class RequestType(models.Model):
    request_type = models.CharField(max_length=255)

    def __str__(self):
        return self.request_type


class Reason(models.Model):
    reason = models.CharField(max_length=255)

    def __str__(self):
        return self.reason


class Request(models.Model):
    partial_day_options = (
        ('AM', 'Buổi sáng'),
        ('PM', 'Buổi chiều'),
        ('ALL', 'Cả ngày'),
    )

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='request_owner')
    created_on = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=255, unique_for_date='created_on')
    request_type = models.ForeignKey(
        RequestType, on_delete=models.PROTECT, default=1)
    start_date = models.DateField()
    end_date = models.DateField()
    partial_day = models.CharField(
        max_length=3, choices=partial_day_options, default='ALL')

    @property
    def duration(self):
        if self.partial_day in ['AM', 'PM'] and abs(self.start_date - self.end_date).days == 0:
            return 0.5
        return np.busday_count(self.start_date, self.end_date) + 1

    reason = models.ForeignKey(
        Reason, on_delete=models.PROTECT, default=1)
    approver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='request_approver')
    detail_reason = models.TextField(blank=True, null=True)
    supervisor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='request_supervisor')
    inform_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='request_inform_to', blank=True, null=True)
    expected_approve = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    objects = models.Manager()

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return f'{self.created_on} {self.owner} {self.request_type}'
