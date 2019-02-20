"""."""

from django.conf.urls import url

from pretalx.event.models.event import SLUG_CHARS

from .views import helloworld
# from .views import rawtable

urlpatterns = [
    url(
        f'^orga/event/(?P<event>[{SLUG_CHARS}]+)/raw_table',
        helloworld.world,
        # rawtable.RawTable.as_view(),
        name='rawtable'
    ),
]
