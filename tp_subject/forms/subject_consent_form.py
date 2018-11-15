from django import forms
from edc_form_validators import FormValidatorMixin
from edc_consent.modelform_mixins import ConsentModelFormMixin
from edc_base.sites.forms import SiteModelFormMixin
from ..models import SubjectConsent
from ..custom_choices import ID_TYPE


class SubjectConsentForm(
        SiteModelFormMixin, FormValidatorMixin, ConsentModelFormMixin, forms.ModelForm):

    screening_identifier = forms.CharField(
        label='Screening Identifier')

    identity_type = forms.CharField(
        label='What type of identity number is provided by subject?',
        widget=forms.RadioSelect(choices=list(ID_TYPE)))

    def clean_gender_of_consent(self):
        return None

    def clean_guardian_and_dob(self):
        return None

    def clean_identity_with_unique_fields(self):
        return None

    class Meta:
        model = SubjectConsent
        fields = '__all__'
        help_texts = {
            'identity': ('Use country ID Number, Passport Number, driver\'s license '
                         'number or country ID receipt number.'),
            'witness_name': ('Required if participant is illitrate. '
                             'Lastname, Firstname of the witness. ')
        }
