from django.shortcuts import get_object_or_404, render

from works.models import Work


# Create your views here.
def get_favouraite_case_studies():
    favCaseStudies = Work.objects.filter(isCaseStudy=True, isFavouraite=True, isPublished=True).order_by(
        "-importanceScore"
    )
    # print("favCaseStudies: ", favCaseStudies)
    return favCaseStudies


def get_favouraite_case_studies_name():
    favCaseStudies = Work.objects.filter(isCaseStudy=True, isFavouraite=True, isPublished=True).order_by(
        "title", "-importanceScore"
    )
    # print("favCaseStudies: ", favCaseStudies)
    return favCaseStudies


def get_favouraite_case_studies_views():
    favCaseStudies = Work.objects.filter(isCaseStudy=True, isFavouraite=True, isPublished=True).order_by(
        "-views", "-importanceScore"
    )
    # print("favCaseStudies: ", favCaseStudies)
    return favCaseStudies


def work_detial_view(request, work_id):
    context = {}
    context["work"] = get_object_or_404(Work, id=work_id)
    print(context)
    return render(request, "pages/work_detail.html", context)
