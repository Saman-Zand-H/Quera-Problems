from django.http import HttpResponseForbidden, HttpResponse, JsonResponse
from django.core.cache import cache
from django.urls import resolve
from datetime import datetime
from django.utils import timezone
from rest_framework import status

from .models import BlockedIp, SecurityConfig, ViewDetail

from .utils import get_client_ip

class DDOSResponse(HttpResponse):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS


class BlockIpMiddleware(object):
    maximum_rps = 4
    timeout = 60

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        view, _, _ = resolve(request.path)
        user_ip = get_client_ip(request)

        is_banned = self.banned_before(user_ip)
        if is_banned:
            return HttpResponseForbidden()
        
        LIMITED_VIEWS = SecurityConfig.objects.last().views.values_list(
            'name',
            flat=True
        )
        
        if view.__name__ in LIMITED_VIEWS:
            data = self._handle_cache(user_ip)
            is_valid_rps = self.validate_request_per_second(user_ip, view.__name__, data)
            
            if not is_valid_rps:
                return DDOSResponse()
        
        return self.get_response(request)

    def banned_before(self, user_ip):
        return BlockedIp.is_ip_blocked(user_ip)
    
    def _handle_cache(self, user_ip):
        key = f"ip_data:{user_ip}"
        data = cache.get(key, dict())
        if not cache.get(key, False):
            data = {"hits": 0, "first_req": timezone.now().timestamp()}
        data["hits"] += 1
        cache.set(key, data, self.timeout)
        return data

    def validate_request_per_second(self, user_ip, view_name, data):
        hits = data.get("hits", 1)
        if hits == 1:
            return True
        
        first_req = data.get("first_req", timezone.now().timestamp())
        delta_time = timezone.now().timestamp() - first_req
        rps = (hits / delta_time) if delta_time != 0 else 0
            
        if rps > self.maximum_rps:
            view_object = ViewDetail.objects.get(name=view_name)
            BlockedIp.objects.create(ip=user_ip,
                                     view=view_object,
                                     rps=int(rps),
                                     created_at=timezone.now())
            cache.set(f"ip_data:{user_ip}", data|{"banned": True})
            return False
        return True
