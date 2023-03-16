from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.db.models import Q
from asgiref.sync import async_to_sync
from .serializer import NameSerializer, NationalIDSerializer
from .models import Hospital, Company, Sick, DeliveryReport, Employee
from .SMS import get_phone_number, sms


@api_view(['POST'])
def get_sick_employee_by_hospital(request):
    data = NameSerializer(data=request.data)
    response = dict()
    if data.is_valid():
        name = data.validated_data.get("name")
        hospital_qs = Hospital.objects.filter(name=name)
        if hospital_qs.exists():
            hospital = hospital_qs.first()
            names = Employee.objects.all().values("name")
            vals = hospital.sicks.filter(
                Q(illName="Covid19")
                & Q(name__in=names)
            ).values_list("name", "nationalID")
            for i, v in enumerate(vals):
                response[i+1] = str(v)
            return Response(data=response, status=HTTP_200_OK)
    return Response(status=HTTP_400_BAD_REQUEST)
        


@api_view(['POST'])
def get_sick_employee_by_company(request):
    data = NameSerializer(data=request.data)
    response = dict()
    if data.is_valid():
        name = data.validated_data.get("name")
        company_qs = Company.objects.filter(name=name)
        if company_qs.exists():
            company = company_qs.first()
            names = company.employees.values("name")
            sicks = Sick.objects.filter(
                Q(illName="Covid19")&Q(name__in=names)).values_list("name", "nationalID")
            for i, v in enumerate(sicks):
                response[i+1] = str(v)
            return Response(response, HTTP_200_OK)
    return Response(status=HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def sms_link(request):
    request.META['CONTENT_LENGTH'] = 35
    data = NationalIDSerializer(data=request.data)
    if data.is_valid():
        ids = [i for i in data.validated_data.get("national_id")]
        phone_numbers = [get_phone_number(i) for i in ids]
        for number in phone_numbers:
            DeliveryReport.objects.create(phone_number=number)
            async_to_sync(sms)(number)
        return Response(status=HTTP_200_OK)
    return Response(status=HTTP_400_BAD_REQUEST)
