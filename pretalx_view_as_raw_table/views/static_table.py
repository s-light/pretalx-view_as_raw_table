"""."""

from django.core import serializers
from django.views.generic import ListView

from pretalx.common.mixins.views import EventPermissionRequired

from pretalx.submission.models import Submission
from pretalx.schedule.models import TalkSlot


class StaticTable_Submissions(EventPermissionRequired, ListView):
    """Raw Table View."""

    model = Submission
    context_object_name = 'submissions'
    template_name = 'pretalx_view_as_raw_table/static_table_submissions.html'
    permission_required = 'orga.view_submissions'

    def get_queryset(self):
        """Prepare queryset."""
        self.qs = (
            self.request.event.submissions(manager='all_objects')
            .select_related('submission_type')
            .order_by('-id')
            .all()
        )
        return self.qs.distinct()

    def get_context_data(self, **kwargs):
        """Prepare context."""
        context = super().get_context_data(**kwargs)
        data = serializers.serialize("python", self.qs.distinct())
        # print(data)
        context['data_set_name'] = 'Submissions'
        context['data_headers'] = []
        context['data_raw'] = data
        for name, value in data[0]['fields'].items():
            # print(name)
            context['data_headers'].append(name)
        context['data_list'] = []
        # print(data[0]['fields'].items())
        # for model, pk, fields in data:
        #     row = []
        #     print(model, pk, fields)
        #     # for name, value in fields:
        #     #     row.append(value)
        #     context['data_list'].append(row)
        return context


class StaticTable_Talks(EventPermissionRequired, ListView):
    """Raw Table View."""

    model = TalkSlot
    context_object_name = 'data'
    template_name = 'pretalx_view_as_raw_table/static_table_talks.html'
    permission_required = 'orga.view_submissions'

    def get_queryset(self):
        """Prepare queryset."""
        qs = (
            self.request.event.talks.order_by('start').all()
        )
        return qs

    def get_context_data(self, **kwargs):
        """Prepare context."""
        context = super().get_context_data(**kwargs)
        return context


def world(request, event):
    """Hello World."""
    from django.http import HttpResponse
    return HttpResponse('Hello World :-) (from the static_table.py)')
