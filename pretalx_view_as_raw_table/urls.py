"""."""

from django.conf.urls import url

from pretalx.event.models.event import SLUG_CHARS

# from .views import helloworld
from .views import rawtable

urlpatterns = [
    # url(
    #     f'^orga/event/(?P<event>[{SLUG_CHARS}]+)/helloworld',
    #     helloworld.world,
    #     name='helloworld'
    # ),
    url(
        f'^orga/event/(?P<event>[{SLUG_CHARS}]+)/raw_table',
        # rawtable.RawTable,
        rawtable.world,
        name='rawtable'
    ),
]
