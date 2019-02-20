from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class PluginApp(AppConfig):
    """Main PluginApp entry point."""
    name = 'pretalx_view_as_raw_table'
    verbose_name = 'pretalx view as raw table plugin'

    class PretalxPluginMeta:
        """Meta."""
        name = ugettext_lazy('pretalx view as raw table plugin')
        author = 'Stefan Krüger'
        description = ugettext_lazy("pretalx plugin to view submissions / talks as real raw tabular data (copy and paste friendly ;-) )")
        visible = True
        version = '0.0.0'

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretalx_view_as_raw_table.PluginApp'
