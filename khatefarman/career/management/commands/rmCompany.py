from django.core.management.base import BaseCommand, CommandError, CommandParser
from career.models import Company


class Command(BaseCommand):
    help = "remove companies"
    
    def add_arguments(self, parser: CommandParser):
        parser.add_argument("companies", nargs="*", type=str)
        parser.add_argument("--all", action="store_true")
    
    def handle(self, *args, **options):
        if options.get("all"):
            Company.objects.all().delete()
            return
            
        for name in options.get("companies"):
            qs = Company.objects.filter(name=name)
            if qs.exists():
                qs.delete()
            else:
                self.stderr.write("%s matching query does not exist." % (name,))
