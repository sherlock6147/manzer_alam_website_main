from django.contrib import admin

from works.forms import WorkForm

# Register your models here.
from works.models import Work


@admin.register(Work)
class WorkModelAdmin(admin.ModelAdmin):
    form = WorkForm
