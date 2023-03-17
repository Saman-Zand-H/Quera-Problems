from django.db import models
from django.utils import timezone
from datetime import timedelta

from .utils import list_views

# Create your models here.

__all__ = ('BlockedIp', 'ViewDetail', 'SecurityConfig')


class ViewDetail(models.Model):
    name = models.CharField(max_length=128)
    path = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.name}, {self.path}'


class BlockedIp(models.Model):
    ip = models.CharField(max_length=64)
    ban_time = models.PositiveIntegerField(default=6 * 60)
    view = models.ForeignKey('guard.ViewDetail', related_name='blocked_ips',
                             on_delete=models.SET_NULL, null=True)
    rps = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_blocked(self):
        return (timezone.now().timestamp() - self.created_at.timestamp()) < self.ban_time

    @staticmethod
    def is_ip_blocked(ip):
        obj = BlockedIp.objects.filter(ip=ip)
        return obj.exists() and obj.latest("created_at").is_blocked

    def __str__(self):
        return f'ip: {self.ip} rps: {self.rps}'


class SecurityConfig(models.Model):
    views = models.ManyToManyField('guard.ViewDetail', related_name='config',
                                   blank=True)

    def __str__(self):
        return f'SecurityConfig'
