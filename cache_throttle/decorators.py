from cache_throttle import utils
from django.core.cache import cache
from django.http import HttpResponse
from functools import wraps
import re


class HttpResponseThrottled(HttpResponse):
    status_code = 429


key_pattern = re.compile("(META|POST|GET):([A-Za-z_]+)")


def throttle(
    action_cost=1,
    maximum_points=10,
    points_per_minute=20,
    block=True,
    keys=("META:REMOTE_ADDR",),
    methods=("POST",)
):
    def decorator(fn):
        @wraps(fn)
        def _wrapped(request, *args, **kwargs):
            request.throttled = False
            request.stamina = None
            try:
                interpreted_keys = []
                for key in keys:
                    match = key_pattern.match(key)
                    interpreted_keys.append(getattr(request, match.groups()[0]).get(match.groups()[1]) if match else key)
                if request.method in methods or not methods:
                    request.stamina = utils.throttle(
                        cache,
                        key=interpreted_keys,
                        decrement=action_cost,
                        maximum_stamina=maximum_points,
                        regenerate_per_hour=points_per_minute*60,
                    )
            except utils.ActionThrottled as e:
                request.stamina = e.args[0]
                request.throttled = True
                if block:
                    return HttpResponseThrottled()
            return fn(request, *args, **kwargs)
        return _wrapped
    return decorator
