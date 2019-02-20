"""."""

from django.urls import resolve, reverse
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, TemplateView, View
from pretalx.orga.signals import nav_event

from pretalx.common.mixins.views import EventPermissionRequired

from pretalx.submission.models import Submission


@receiver(nav_event, dispatch_uid='pretalx_view_as_raw_table__submissions')
def navbar_info(sender, request, **kwargs):
    """."""
    url = resolve(request.path_info)
    if not request.user.has_perm('can_see_orga_area', request.event):
        return []
    return [{
        'label': _('Raw Table'),
        'icon': 'table',
        'url': reverse('plugins:pretalx_view_as_raw_table:index', kwargs={
            'event': request.event.slug,
        }),
        'active': (
            url.namespace == 'plugins:pretalx_view_as_raw_table'
            and url.url_name == 'view'
        ),
    }]


class RawTable(EventPermissionRequired, ListView):
    """Raw Table View."""

    model = Submission
    context_object_name = 'test'
    # template_name = 'pretalx_view_as_raw_table/submission/table.html'
    template_name = 'pretalx_view_as_raw_table/test.html'
    permission_required = 'orga.view_submissions'

    # def dispatch(self, *args, **kwargs):
    #     if self.request.user.has_perm('orga.view_speakers', self.request.event):
    #         self.default_filters.add('speakers__name__icontains')
    #     return super().dispatch(*args, **kwargs)
    # #
    # # def get_queryset(self):
    # #     qs = (
    # #         self.request.event.submissions(manager='all_objects')
    # #         .select_related('submission_type')
    # #         .order_by('-id')
    # #         .all()
    # #     )
    # #     return qs.distinct()
    # #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    # #     dates = data.keys()
    # #     if len(dates) > 1:
    # #         date_range = rrule.rrule(
    # #             rrule.DAILY,
    # #             count=(max(dates) - min(dates)).days + 1,
    # #             dtstart=min(dates),
    # #         )
    # #         if len(data) > 1:
    # #             context['timeline_data'] = json.dumps(
    # #                 [
    # #                     {"x": date.isoformat(), "y": data.get(date.date(), 0)}
    # #                     for date in date_range
    # #                 ]
    # #             )
    # #     return context


def world(request, event):
    """Hello World."""
    from django.http import HttpResponse
    return HttpResponse('Hello World')
