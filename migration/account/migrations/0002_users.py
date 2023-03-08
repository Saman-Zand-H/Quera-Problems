from django.conf import settings
from django.db import migrations
import django.utils.timezone
import json 


def create_users(apps, _):
    User = apps.get_model("account", "User")
    
    with open(settings.BASE_DIR / 'account/fixtures/users.json', 'r') as u:
        users = json.load(u)
    
    for user in users:
        try:
            User.objects.get_or_create(username=user["fields"]["username"],
                                    password=user["fields"]["password"])
        except:
            pass
        

class Migration(migrations.Migration):
    dependencies = (
        ("account", "0001_initial"),
    )        
    
    operations = [
        migrations.RunPython(
            code=create_users,
            reverse_code=migrations.RunPython.noop
        )
    ]
