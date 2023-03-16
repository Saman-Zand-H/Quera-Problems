from django.core.management.base import BaseCommand, CommandError, CommandParser
from django.core.validators import EmailValidator
from career.models import Company


def validate_phone(val:str):
    if (
        (val.startswith("09") and len(val)==11)
        or (val.startswith("+98") and len(val)==13)
        or (val.startswith("0098") and len(val)==14)
    ):
        return True
    return False


def validate_email(val:str):
    validator = EmailValidator()
    try:
        validator(val)
        return True
    except:
        return False


class Command(BaseCommand):
    help = "A command to edit a company by it's name"
    
    def add_arguments(self, parser: CommandParser):
        parser.add_argument("current_name", nargs="+", type=str)
        parser.add_argument("--name", nargs="*", type=str)
        parser.add_argument("--email", nargs="*", type=str)
        parser.add_argument("--phone", nargs="*", type=str)
        parser.add_argument("--description", nargs="*", type=str)
        
    def handle(self, *args, **options):
        current_name = options.get("current_name", [])
        if isinstance(current_name, list):
            current_name = " ".join(options.get("current_name", []))
        current_name = str(current_name)
            
        if len(current_name) > 50:
            raise CommandError(
                "Error: Ensure this value has at most 50 characters (it has %d)." 
                % (len(current_name),)
            )
            
        qs = Company.objects.filter(name=current_name)
        if not qs.exists():
            raise CommandError("Company matching query does not exist.")
        
        required_fields = [
            i
            for i in 
            ["name", "email", "phone", "description"]
            if not Company._meta.get_field(i).null
        ]
        
        for field in required_fields:
            detail = str(options.get(field))
            if (
                not bool(getattr(qs.first(), field))
                or (
                    (
                        detail == ['']
                        or detail == []
                        or detail == ''
                    )
                    and field in required_fields               
                )
            ):
                raise CommandError("%s cannot be blank." % (field.title(),))
            
        name = options.get("name", [])
        if isinstance(name, list):
            name = " ".join(name)
            
        email = options.get("email", [])
        if isinstance(email, list):
            email = " ".join(email)
            
        phone = options.get("phone", [])
        if isinstance(phone, list):
            phone = " ".join(phone)
            
        desc = options.get("description", [])
        if isinstance(desc, list):
            desc = " ".join(desc)
            
        values = dict()
        
        if bool(phone):
            if validate_phone(phone):
                values["phone"] = phone
            else:
                raise CommandError("Error: Phone number format is not valid.")
        
        if bool(email):
            if validate_email(email):
                values["email"] = email
            else:
                raise CommandError("Error: Enter a valid email address.")
        
        if bool(name):
            if len(name) >= 50:
                raise CommandError(
                    "Error: Ensure this value has at most 50 characters (it has %d)." 
                    % (len(name),)
                )
            elif Company.objects.filter(name=name).exists() and name != current_name:
                raise CommandError("Error: That name is already taken.")
            else:
                values["name"] = name.strip()
        
        if bool(desc):
            values["description"] = desc
        
        Company.objects.filter(name=current_name).update(**values)
            