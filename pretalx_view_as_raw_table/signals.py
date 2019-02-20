"""Register your receivers here."""

from django.dispatch import receiver
from django.urls import resolve, reverse
# from django.utils.timezone import now
# from pretalx.agenda.signals import register_recording_provider
# from pretalx.common.signals import periodic_task
# from pretalx.event.models import Event
# from pretalx.orga.signals import nav_event_settings
from pretalx.orga.signals import nav_event


@receiver(nav_event, dispatch_uid='pretalx_view_as_raw_table')
def navbar_info(sender, request, **kwargs):
    """Register button in orga navigation bar."""
    url = resolve(request.path_info)
    can_see_orga_area = request.user.has_perm(
        'orga.view_orga_area',
        request.event
    )
    if not can_see_orga_area:
        return []
    return [
        # {
        #     'label': 'Raw Table',
        #     'icon': 'table',
        #     'url': reverse(
        #         'plugins:pretalx_view_as_raw_table:rawtable',
        #         kwargs={'event': request.event.slug}
        #     ),
        #     'active': (
        #         url.namespace == 'plugins:pretalx_view_as_raw_table'
        #         and url.url_name == 'rawtable'
        #     ),
        # },
        {
            'label': 'Static Table - Submissions',
            'icon': 'table',
            'url': reverse(
                'plugins:pretalx_view_as_raw_table:static_table.submissions',
                kwargs={'event': request.event.slug}
            ),
            'active': (
                url.namespace == 'plugins:pretalx_view_as_raw_table'
                and url.url_name == 'static_table.submissions'
            ),
        },
        {
            'label': 'Static Table - Talks',
            'icon': 'table',
            'url': reverse(
                'plugins:pretalx_view_as_raw_table:static_table.talks',
                kwargs={'event': request.event.slug}
            ),
            'active': (
                url.namespace == 'plugins:pretalx_view_as_raw_table'
                and url.url_name == 'static_table.talks'
            ),
        },
    ]
