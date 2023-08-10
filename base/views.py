from django.shortcuts import render

# from works.models import Work
from works.views import (
    get_favouraite_case_studies,
    get_favouraite_case_studies_name,
    get_favouraite_case_studies_views,
)

# from django.views.generic import ListView, TemplateView


def home(request):
    context = {}
    context["favCaseStudies"] = get_favouraite_case_studies()
    context["favCaseStudiesName"] = get_favouraite_case_studies_name()
    context["favCaseStudiesViews"] = get_favouraite_case_studies_views()
    return render(request, "pages/home.html", context)
