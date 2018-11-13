from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from ..models import SubjectVisit


class SubjectModelFormMixin(SiteModelFormMixin, FormValidatorMixin, forms.Form):

    visit_model = SubjectVisit
