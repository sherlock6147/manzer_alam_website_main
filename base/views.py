from django.shortcuts import render

# from works.models import Work
from works.views import get_favouraite_case_studies

# from django.views.generic import ListView, TemplateView


def home(request):
    context = {}
    context["favCaseStudies"] = get_favouraite_case_studies()
    return render(request, "pages/home.html", context)
