"""."""

from django.urls import resolve, reverse
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, TemplateView, View
from pretalx.orga.signals import nav_event

from pretalx.common.mixins.views import EventPermissionRequired

from pretalx.submission.models import Submission

class RawTable(EventPermissionRequired, TemplateView):
    """Raw Table View."""

    # context_object_name = 'helper'
    template_name = 'pretalx_view_as_raw_table/table.html'
    permission_required = 'orga.view_submissions'

    def get_context_data(self, **kwargs):
        """Prepare context."""
        context = super().get_context_data(**kwargs)
        api_base = self.request.event.api_urls.base
        doc_base = 'https://pretalx.readthedocs.io/en/latest/api/resources/'
        context['data_source'] = [
            {
                'label': 'Submissions',
                'url': api_base + 'submissions',
                'doc': doc_base + 'submissions.html#submissions',
            },
            {
                'label': 'Talks',
                'url': api_base + 'talks',
                'doc': doc_base + 'talks.html#talks',
            },
        ]
        return context


# class RawTable(EventPermissionRequired, ListView):
#     """Raw Table View."""
#
#     model = Submission
#     context_object_name = 'test'
#     # template_name = 'pretalx_view_as_raw_table/helloworld.html'
#     # template_name = 'pretalx_view_as_raw_table/test.html'
#     template_name = 'pretalx_view_as_raw_table/table.html'
#     permission_required = 'orga.view_submissions'
#
#     def get_queryset(self):
#         """Prepare queryset."""
#         qs = (
#             self.request.event.submissions(manager='all_objects')
#             .select_related('submission_type')
#             .order_by('-id')
#             .all()
#         )
#         return qs.distinct()
#
#     def get_context_data(self, **kwargs):
#         """Prepare context."""
#         context = super().get_context_data(**kwargs)
#         # dates = data.keys()
#         # if len(dates) > 1:
#         #     date_range = rrule.rrule(
#         #         rrule.DAILY,
#         #         count=(max(dates) - min(dates)).days + 1,
#         #         dtstart=min(dates),
#         #     )
#         #     if len(data) > 1:
#         #         context['timeline_data'] = json.dumps(
#         #             [
#         #                 {"x": date.isoformat(), "y": data.get(date.date(), 0)}
#         #                 for date in date_range
#         #             ]
#         #         )
#         return context
