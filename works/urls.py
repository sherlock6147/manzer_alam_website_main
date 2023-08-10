from django.urls import path

from works.views import work_detial_view

app_name = "works"

urlpatterns = [
    path("<int:work_id>", view=work_detial_view, name="detail"),
]
