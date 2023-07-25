from django.urls import path

from base.views import HomeView

app_name = "base"

urlpatterns = [
    path("", view=HomeView.as_view(), name="home"),
]
