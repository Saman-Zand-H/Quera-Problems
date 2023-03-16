from django.http import JsonResponse, HttpResponseForbidden, HttpResponse

from django.core.cache import cache
from django.urls import resolve
from datetime import datetime
from django.utils import timezone
from rest_framework import status

from .models import BlockedIp, SecurityConfig, ViewDetail

from .utils import get_client_ip


class DDOSResponse(HttpResponse):
    status_code = 429


class BlockIpMiddleware(object):
    maximum_rps = 1
    timeout = 60

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.path = request.path
        self.user_ip = get_client_ip(request)
        LIMITED_VIEWS = SecurityConfig.objects.last().views.values_list(
            'path',
            flat=True
        )

        is_banned = self.banned_before(self.user_ip)
        if is_banned:
            return HttpResponseForbidden()

        self._handle_cache()
        if not self.validate_request_per_second():
            return DDOSResponse()
        
        return self.get_response(request)

    def banned_before(self, user_ip):
        return BlockedIp.is_ip_blocked(user_ip)
    
    def _handle_cache(self):
        self.req_key = f"{self.user_ip}:req"
        self.time_key = f"{self.user_ip}:time"
        
        if not cache.get(self.req_key):
            cache.set(self.req_key, 1, self.timeout)
        else:
            cache.incr(self.req_key, 1)
            
        if not cache.get(self.time_key):
            cache.set(self.time_key, timezone.now().isoformat(), timeout=60)
        

    def validate_request_per_second(self, *args, **kwargs):
        reqs = int(cache.get(self.req_key))
        time = cache.get(self.time_key)
        time_delta = (timezone.now() - datetime.fromisoformat(time)).microseconds
        rps = reqs/(time_delta*10**6)
            
        if rps > self.maximum_rps:
            view_object = ViewDetail.objects.get(path=self.path)
            BlockedIp.objects.create(ip=self.ip,
                                     view=view_object,
                                     rps=int(rps))
            return False
        return True
