# جلال و جلالی

جَلال انسانی وطن‌دوست و میهن‌پرست است.

او که از کار کردن با تقویم میلادی و تبدیل دائم آن به تقویم شمسی خسته شده بود، از شما برای رفع این مشکل درخواست کمک کرده است. از آن‌جایی که شما نیز انسانی وطن‌دوست و میهن‌پرست هستید، با کمال میل به کمک او می‌شتابید و به جَلال کمک می‌کنید تا با تقویم جَلالی کار کند.

در این پروژه شما باید قابلیت اضافه‌کردن تاریخ فارسی به مدل جنگو را با استفاده از کتابخانه‌ی django_jalali پیاده‌سازی کنید.

مدل CustomUser
اپلیکیشن Users فقط شامل یک مدل به نام CustomUser است که این مدل شامل فیلدهای زیر می‌باشد:

ویژگی‌ها
ویژگی ‍‍username : این فیلد از نوع CharField و حداکثر طول آن ۲۵۶ می‌باشد.
ویژگی ‍‍full_name : این فیلد از نوع CharField و حداکثر طول آن ۲۵۶ می‌باشد.
ویژگی gender : این فیلد از نوع CharField می‌باشد. ویژگی gender باید از بین جنسیت‌های Male و Female انتخاب شود و در داخل پایگاه داده به جای Male حرف M ذخیره و به جای کلمه‌ی Female حرف F ذخیره شود.
ویژگی ‍‍national_code : این فیلد از نوع CharField و حداکثر طول آن ۱۰ می‌باشد.
ویژگی birthday_date : این فیلد از نوع تاریخ (‍date) شمسی می‌باشد.
ویژگی ceremony_datetime : این فیلد از نوع تاریخ و ساعت (datetime) شمسی می‌باشد.
ویژگی country :‌ این فیلد از نوع CharField است و مقدار آن، برای همه‌ی شئ‌ها برابر رشته‌ی Iran است.

تابع get_first_and_last_name : این تابع، first_name و last_name کاربر را از روی فیلد full_name بدست آورده و در قابل یک دیکشنری بازمی‌گرداند. تضمین می‌شود که فیلد full_name فقط شامل یک فاصله (آن هم بین first_name و last_name) می‌باشد.

تابع get_age : این تابع، سن کاربر را از روی فیلد birthday_date محاسبه کرده و بازمی‌گرداند. دقت کنید که این تابع باید جزء صحیح سن را بازگرداند. مثلا اگر شخصی ۵ سال و ۳ ماه سن داشت، باید عدد ۵ را بازگرداند یا اگر شخصی ۱۰ سال و ۱۱ ماه داشت باید عدد ۱۰ را بازگرداند.

تابع is_birthday : این تابع مشخص می‌کند که آیا امروز، روز تولد کاربر مورد نظر هست یا خیر. در صورتی که امروز، روز تولد کاربر بود، مقدار True و در غیر این‌صورت، مقدار ‌False را بازمی‌گرداند.

فرم CustomUserForm
تمامی فیلدهای مدل CustomUser باید داخل کلاس CustomUserForm در فایل ‍‍forms.py وجود داشته باشند.

اعتبارسنجی‌ها:

فیلد national_code باید دقیقا شامل ۱۰ کاراکتر باشد.
فیلد full_name باید حتماً شامل first_name و last_name باشد و هر دوی این مقادیر باید عنوان باشند. عنوان‌ بودن یعنی با یک حرف بزرگ انگلیسی شروع شده و بقیه‌ی حروف هر کلمه کوچک باشند.

ادمین
مدل‌ CustomUser موجود در models.py باید در پنل ادمین ثبت شده و قابل مشاهده باشد.

شخصی‌سازی CustomUserAdmin
در لیست CustomUserها، مقادیر زیر نمایش داده شود (ترتیب مهم نیست):
username
first_name
last_name
gender
national_code
birthday_date
توجه: فیلدهای first_name و last_name از روی فیلد full_name ایجاد می‌شوند.

قابلیت جستجو بر اساس username و full_name وجود داشته باشد.

لیست CustomUserها براساس ceremony_datetime، به صورت صعودی مرتب شده باشد.

link: <https://quera.org/problemset/129725/>