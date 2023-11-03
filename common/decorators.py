from functools import wraps
from django.http import HttpResponseBadRequest


# when a function was designed only with HTMX in mind
def htmx_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.headers.get('HX-Request'):
            return HttpResponseBadRequest("Invalid request")
        return view_func(request, *args, **kwargs)
    return _wrapped_view