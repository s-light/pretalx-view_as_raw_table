"""."""

from django.views.generic import ListView

from pretalx.common.mixins.views import EventPermissionRequired

from pretalx.submission.models import Submission


class StaticTable(EventPermissionRequired, ListView):
    """Raw Table View."""

    model = Submission
    context_object_name = 'data'
    template_name = 'pretalx_view_as_raw_table/static_table.html'
    permission_required = 'orga.view_submissions'

    def get_queryset(self):
        """Prepare queryset."""
        qs = (
            self.request.event.submissions(manager='all_objects')
            .select_related('submission_type')
            .order_by('-id')
            .all()
        )
        return qs.distinct()

    def get_context_data(self, **kwargs):
        """Prepare context."""
        context = super().get_context_data(**kwargs)
        # dates = data.keys()
        # if len(dates) > 1:
        #     date_range = rrule.rrule(
        #         rrule.DAILY,
        #         count=(max(dates) - min(dates)).days + 1,
        #         dtstart=min(dates),
        #     )
        #     if len(data) > 1:
        #         context['timeline_data'] = json.dumps(
        #             [
        #                 {"x": date.isoformat(), "y": data.get(date.date(), 0)}
        #                 for date in date_range
        #             ]
        #         )
        return context


def world(request, event):
    """Hello World."""
    from django.http import HttpResponse
    return HttpResponse('Hello World :-) (from the static_table.py)')
