from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "manzer_alam_main_website.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import manzer_alam_main_website.users.signals  # noqa: F401
        except ImportError:
            pass
