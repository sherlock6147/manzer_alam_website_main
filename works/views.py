# from django.shortcuts import render

from works.models import Work


# Create your views here.
def get_favouraite_case_studies():
    favCaseStudies = Work.objects.filter(isCaseStudy=True, isFavouraite=True, isPublished=True).order_by(
        "-importanceScore"
    )
    print("favCaseStudies: ", favCaseStudies)
    return favCaseStudies
