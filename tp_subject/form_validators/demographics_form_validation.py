from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from edc_form_validators import FormValidator
from edc_constants.constants import MALE, FEMALE


class DemographicsFormValidator(FormValidator):

    subject_consent_model = 'tp_subject.subjectconsent'

    def subject_consent_model_cls(self):
        return django_apps.get_model(self.subject_consent_model)

    def clean(self):
        self.validate_marital(cleaned_data=self.cleaned_data)

    def validate_marital(self, cleaned_data=None):
        try:
            subject_consent = self.subject_consent_model_cls.objects.get(
                subject_identifier=cleaned_data.get('subject_visit').appointment.subject_identifier)

            fields_applicable = {FEMALE: 'number_of_spouses_f',
                                 MALE: 'number_of_spouses_m'}
            condition = (cleaned_data.get('marital_status') == 'Married')
            self.applicable_if_true(
                condition=condition,
                field_applicable=fields_applicable.get(subject_consent.gender))

        except ObjectDoesNotExist:
            raise ValidationError("Subject Consent Form not completed.")
