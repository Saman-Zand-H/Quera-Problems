from django.core.management.base import BaseCommand

from apps.guard.models import SecurityConfig, ViewDetail
from apps.guard.utils import list_views


class Command(BaseCommand):
    """ This command initializes the gurad
        for enhancing the security of your project.
    """
    help = 'Initialize Guard app'
    requires_migrations_checks = True

    def handle(self, *args, **kwargs):
        if SecurityConfig.objects.count() != 1:
            SecurityConfig.objects.all().delete()
            SecurityConfig.objects.create()
            
        sec = SecurityConfig.objects.first()
        ViewDetail.objects.all().delete()
        ViewDetail.objects.bulk_create([
            ViewDetail(name=name, path=path)
            for path, name in list_views()
        ])
        for url, name in list_views():
            sec.views.add(ViewDetail.objects.get(path=url, name=name))
