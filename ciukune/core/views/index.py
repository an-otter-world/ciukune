"""Home page view, loading Ciukune apps from local rollup development server, or built assets in production."""
from django.apps import apps
from django.conf import settings
from django.views.generic import TemplateView

from ciukune.core.utils.apps import CiukuneAppConfig

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stylesheets = []
        scripts = []
        if settings.DEBUG_UI:
            scripts = ['http://localhost:3000/src/main.ts']
        else:
            configs = [it for it in apps.get_app_configs() if isinstance(it, CiukuneAppConfig)]
            for config in configs:
                scripts.append(f'static/ui/js/{config.name}.js')
                stylesheets.append(f'static/ui/css/{config.name}.css')
        context['scripts'] = scripts
        context['stylesheets'] = stylesheets
        return context
