# فاکتوریسم

در این سوال شما باید یک کلاس مدیریت فاکتورهای فروش برای شرکت سجادینه طراحی کنید. در شرکت سجادینه افراد زیادی می‌توانند فاکتورهای مالی را ثبت کنند و هر کدام از این افراد تاریخ فاکتور را به یکی از ۶ فرمتی که در جدول پایین آمده ثبت می‌کنند.

برای مثال یک فاکتور که روز دوم ماه ششم سال ۲۰۲۰ ثبت شود، می‌تواند طبق یکی از فرمت‌های زیر ثبت شود:

dd/mm/yyyy‍
dd/yyyy‍/mm
yyyy‍/mm/dd
yyyy‍/dd/mm
mm/yyyy‍/dd
mm/dd/yyyy‍

شما باید کلاس ‍‍FactorHandler را در این فایل کامل کنید به طوری که سه تابع زیر عملکردهای خواسته شده را داشته باشند (عملکرد تابع __init__ اهمیت ندارد).

```python
class FactorHandler:
    def __init__(self):
        pass

    def add_factor(self, time_format, time, value):
        pass

    def remove_all_factors(self, time_format, time):
        pass

    def get_sum(self, time_format, start_time, finish_time):
        pass
```

در همه توابع تضمین می‌شود که time حتما بر حسب فرمت time_format است. توجه کنید که هیچ یک از توابع بالا را نباید استاتیک تعریف کنید.

link: <https://quera.org/problemset/76277/>
