"""."""

from django.conf.urls import url

from pretalx.event.models.event import SLUG_CHARS

# from .views import helloworld
# from .views import rawtable
from .views import static_table

urlpatterns = [
    # url(
    #     f'^orga/event/(?P<event>[{SLUG_CHARS}]+)/raw_table',
    #     # helloworld.world,
    #     rawtable.RawTable.as_view(),
    #     name='rawtable'
    # ),
    url(
        f'^orga/event/(?P<event>[{SLUG_CHARS}]+)/submissions/static_table',
        static_table.StaticTable.as_view(),
        name='static_table'
    ),
]
