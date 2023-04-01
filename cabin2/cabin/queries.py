from cabin.models import *
from django.db.models import Sum, F, Count, Q, FloatField, Subquery, OuterRef, Case, When, IntegerField
from django.db.models.functions import Cast, Coalesce
from django.db.models.lookups import GreaterThan, GreaterThanOrEqual
import math


def query_0(x):
    q = Driver.objects.filter(rating__gt=x)
    return q


def query_1(x):
    q = Payment.objects.filter(
        ride__car__owner__id=x).aggregate(
            payment_sum=Sum("amount"))
    return q

def query_2(x):
    q = (Ride.objects.filter(request__rider__id=x))
    return q


def query_3(t:int):
    q = (
        Ride
        .objects
        .all()
        .aggregate(
            vals=Count(
                "id",
                filter=GreaterThan(
                    F("dropoff_time") - F("pickup_time"),
                    t
                )
            )
        )["vals"]
    )
    return q


def query_4(x, y, r):
    return (
        Driver
        .objects
        .filter(active=True)
        .annotate(
            distance=Cast(((F("x")-(x))**2 + (F("y")-(y))**2)**.5, FloatField())
        )
        .filter(distance__lte=r)
    )


def query_5(n, c):
    q = (
        Driver
        .objects
        .annotate(
            ride_count=Count(F("car__ride"))
        )
        .filter((Q(car__car_type="A") | Q(car__color=c)) & Q(ride_count__gte=n))
        .distinct()
    )
    return q


def query_6(x, t):
    q = (
        Rider
        .objects
        .annotate(ride_count=Count(F("riderequest__ride")))
        .annotate(total_payment=Sum(F("riderequest__ride__payment__amount")))
        .filter(
            Q(ride_count__gte=x)
            & Q(total_payment__gt=t)
        )
    )
    return q


def query_7():
    subq = Subquery(
        Ride
        .objects
        .filter(car__owner__id=OuterRef("id"))
        .filter(request__rider__account__first_name=OuterRef("account__first_name"))
        .values("id")
    )
    q = (
        Driver.objects.filter(car__ride__id__in=subq).distinct()
    )
    return q


def query_8():
    subq = Subquery(
        Ride
        .objects
        .filter(
            Q(car__owner__id=OuterRef("id"))
            & Q(request__rider__account__last_name=OuterRef("account__last_name"))
        )
        .values("car__owner")
        .annotate(c=Count("id"))
        .values("c")
    )
    q = (
        Driver
        .objects
        .annotate(n=Coalesce(subq, 0))
    )
    return q


def query_9(x, t):
    q = (
        Driver
        .objects
        .annotate(
            n=Count(
                "car__ride__id",
                filter=(
                    Q(
                        car__model__gte=x
                    )
                    & Q(
                        GreaterThanOrEqual(
                            F("car__ride__dropoff_time")
                            - F("car__ride__pickup_time"),
                            t
                        )
                    )
                )
            )
        )
        .values("id", "n")
    )
    return q


def query_10():
    q = (
        Car
        .objects
        .annotate(
            extra=Case(
                When(car_type="A", then=Count("ride__id",
                                              output_field=IntegerField())),
                When(
                    car_type="B", 
                    then=Sum(F("ride__dropoff_time")-F("ride__pickup_time"), 
                             output_field=IntegerField())
                ),
                When(
                    car_type="C",
                    then=Sum("ride__payment__amount",
                             output_field=IntegerField())
                )
            )
        )
    )
    return q
