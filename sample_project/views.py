from django.http import HttpResponse
from cache_throttle.decorators import throttle


@throttle()
def blocking(request):
    return HttpResponse("Success")


@throttle(block=False)
def nonblocking(request):
    return HttpResponse("Success" if not request.throttled else "Throttled")


@throttle(keys=("META:REMOTE_ADDR", "Something else"), points_per_minute=5)
def slow_and_manualkey(request):
    return HttpResponse("Success")
