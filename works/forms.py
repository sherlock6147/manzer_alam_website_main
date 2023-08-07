from django import forms
from pagedown.widgets import AdminPagedownWidget

from works.models import Work


class WorkForm(forms.ModelForm):
    description = forms.CharField(widget=AdminPagedownWidget())
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Work
        fields = "__all__"
