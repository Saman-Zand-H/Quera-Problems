from django.core.management import BaseCommand
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
    help = "add new company"
    nullables = [
        i
        for i in ["name", "email", "phone", "description"]
        if Company._meta.get_field(i).null
    ]
    
    def _validate_name(self, val):
        # Check nullability
        if len(val) == 0 and "name" not in self.nullables:
            self.stderr.write("Error: This field cannot be blank.")
            return self._validate_name(str(input("Name: ")).strip())
        elif len(val) == 0 and "name" in self.nullables:
            return None

        if len(val) > 50:
            self.stderr.write(
                "Error: Ensure this value has at most 50 characters (it has %d)."
                % (len(val),)
            )
            return self._validate_name(str(input("Name: ")).strip())
            
        if Company.objects.filter(name=val).exists():
            self.stderr.write("Error: That name is already taken.")
            return self._validate_name(str(input("Name: ")).strip())

        return val
    
    def _validate_email(self, val):
        if len(val) == 0 and "email" not in self.nullables:
            self.stderr.write("Error: This field cannot be blank.")
            return self._validate_email(str(input("Email: ")).strip())
        elif len(val) == 0 and "email" in self.nullables:
            return None
            
        elif not validate_email(val):
            self.stderr.write("Error: Enter a valid email address.")
            return self._validate_email(str(input("Email: ")).strip())
        
        return val
    
    def _validate_phone(self, val):
        if len(val) == 0 and "phone" not in self.nullables:
            self.stderr.write("Error: This field cannot be blank.")
            return self._validate_phone(str(input("Phone: ")).strip())
        elif len(val) == 0 and "phone" in self.nullables:
            return None
            
        if not validate_phone(val):
            self.stderr.write("Error: Phone number format is not valid.")
            return self._validate_phone(str(input("Phone: ")).strip())
            
        return val
    
    def _validate_desc(self, val):
        if len(val) == 0 and "description" not in self.nullables:
            self.stderr.write("Error: This field cannot be blank.")
            return self._validate_desc(str(input("Description: ")).strip())
        elif len(val) == 0 and "description" in self.nullables:
            return None
        return val
    
    def handle(self, *args, **options):
        name = self._validate_name(str(input("Name: ")).strip())
        email = self._validate_email(str(input("Email: ")).strip())
        phone = self._validate_phone(str(input("Phone: ")).strip())
        description = self._validate_desc(str(input("Description: ")).strip())
        
        Company.objects.create(name=name,
                               email=email,
                               phone=phone,
                               description=description)
    