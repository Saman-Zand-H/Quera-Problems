from django.db.models import F, Sum, Count, Case, When, IntegerField
from django.db.models.lookups import GreaterThanOrEqual, GreaterThan
from .models import (
    Employee, 
    Payslip, 
    Payment, 
    Salary, 
    EmployeeProjectRelation as EPRel,
    Department
)


def query_0():
    q = Employee.objects.all()
    return q


def query_1():
    return (
        Payslip
        .objects
        .filter(payment=None)
        .aggregate(
            total_dept=Sum(F("tax")
                           +F("overtime")
                           +F("base")
                           +F("insurance"))
            )
        )


def query_2(x:int):
    return (
        Payslip
        .objects
        .filter(salary__overtime__gte=x)
        .aggregate(total_overtime=Sum(F("overtime")))
    )


def query_3():
    return Payment.objects.all().aggregate(total=Sum(F("amount")))


def query_4(x:int):
    ep_qs = EPRel.objects.filter(employee=x)
    return ep_qs.aggregate(total_hours=Sum(F("hours")))


def query_5(x):
    salaries = (
        Salary
        .objects
        .all()
        .annotate(income=Sum(F("payslip__payment__amount")))
        .filter(income__gt=x)
    )
    return Employee.objects.filter(salary__in=salaries)
    


def query_6():
    return (
        Employee
        .objects
        .all()
        .annotate(total_hours=Sum(
            F("employeeprojectrelation__hours")))
        .order_by("-total_hours", "account__username")
        .first()
    )


def query_7():
    return (
        Department
        .objects
        .all()
        .annotate(
            total=Sum(F("employee__salary__payslip__payment"))
        )
        .order_by("-total", "name")
        .first()
    )


def query_8():
    return (
        Department
        .objects
        .all()
        .annotate(
            num=Count(
                F("project"),
                filter=GreaterThanOrEqual(
                    F("project__estimated_end_time")
                    -F("project__end_time"),
                    0
                )
            )
        )
        .order_by("-num", "project__title")
        .first()
    )


def query_9(x):
    return (
        Employee
        .objects
        .all()
        .annotate(
            num=Count(
                F("attendance"),
                filter=GreaterThan(
                    x
                    -F("attendance__in_time"),
                    0
                )
            )
        )
        .order_by("-num", "account__username")
        .first()
    )


def query_10():
    return {"total": Employee.objects.filter(employeeprojectrelation=None).count()}
