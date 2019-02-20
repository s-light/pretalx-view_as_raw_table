"""."""

from django.http import HttpResponse


def world(request, event):
    """Hello World."""
    return HttpResponse('Hello World')
