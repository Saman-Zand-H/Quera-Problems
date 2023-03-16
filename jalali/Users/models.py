from django.db import models
from django.utils import timezone
from django_jalali.db import models as jmodels
import jdatetime
from django.core.exceptions import ValidationError

class CustomUser(models.Model):
    GENDERS = (
        ("M", "Male"),
        ("F", "Female")
    )
    COUNTRIES = (("Iran", "Iran"),)
    username = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDERS)
    national_code = models.CharField(max_length=10)
    birthday_date = jmodels.jDateField()
    ceremony_datetime = jmodels.jDateTimeField()
    country = models.CharField(max_length=4, 
                               default="Iran", 
                               choices=COUNTRIES, 
                               blank=True)
    
    class Meta:
        ordering = ("-ceremony_datetime",)

    def get_first_and_last_name(self):
        l = self.full_name.split(" ")
        return {"first_name": l[0], "last_name": l[1]}

    def get_age(self):
        jalali_now = timezone.localtime(timezone.now())
        jalali_today = jdatetime.date.fromgregorian(date=jalali_now)
        birthdate = self.birthday_date
        age_years = jalali_today.year - birthdate.year
        if jalali_today.month < birthdate.month:
            age_years -= 1
        elif jalali_today.month == birthdate.month and jalali_today.day < birthdate.day:
            age_years -= 1
        return age_years
    
    def is_birthday(self):
        tz = timezone.localtime(timezone.now())
        birth_day = self.birthday_date.day
        birth_month = self.birthday_date.month
        this_day = jdatetime.date.fromgregorian(date=tz)
        return True if (this_day.month == birth_month and this_day.day == birth_day) else False

    def clear(self, *args, **kwargs):
        name = self.full_name.split(" ")
        if len(name) == 2:
            self.full_name = " ".join([i.title() for i in name])
            return super().save(*args, **kwargs)
        raise ValidationError("Invalid full name.")
