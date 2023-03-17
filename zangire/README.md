# زنجیره

در این تمرین باید کلاسی به نام Chain طراحی کنید به طوری که رفتارهای زیر را داشته باشد:

جمع زنجیره‌ای اعداد
وقتی یک یا چند عدد (چه صحیح چه اعشاری) به صورت زنجیروار به عنوان پارامتر به کلاس ارسال می‌شوند، خروجی باید یک عدد حاصل جمع اعداد ورودی باشد. همچنین خود اشیا باید با مقدار خروجی برابر باشند.

```python
>>> Chain(2.5)(2)(2)(2.5) # sum
9
>>> Chain(3)(1.5)(2)(3) # sum
9.5

>>> Chain(64) == 64
True
```

الحاق زنجیره‌ای رشته‌ها
وقتی یک یا چند رشته به صورت زنجیروار به عنوان پارامتر به کلاس ارسال می‌شوند، خروجی باید یک رشته حاصل الحاق رشته‌های ورودی با یک کاراکتر فاصله (به‌عنوان جدا کننده) باشد. همچنین خود اشیا باید با مقدار خروجی برابر باشند.

```python
>>> Chain('Ali')('Safinal')('is')('the')('best.') # concat with space
'Ali Safinal is the best.'

>>> Chain('abc')('defg') == 'abc defg'
True
```

حالت‌های دیگر
در دو حالت زیر باید یک Exception با پیغام invalid operation پرتاب شود:

یک یا چند رشته و عدد، هم‌زمان به صورت زنجیروار به عنوان پارامتر به کلاس ارسال می‌شوند.
هر پارامتری که از جنس رشته یا عدد نباشد به کلاس ارسال شود.

```python
>>> Chain('Ali')(5) # raising exception with the following message
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
Exception: invalid operation

>>> Chain(9)([1, 2]) # raising exception with the following message
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
Exception: invalid operation
```

link: <https://quera.org/problemset/129729/>
