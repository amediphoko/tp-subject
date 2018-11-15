from django.apps import apps as django_apps
from edc_consent.consent import Consent
from edc_constants.constants import FEMALE, MALE
from edc_consent.site_consents import site_consents

edc_protocol = django_apps.get_app_config('edc_protocol')

v1 = Consent(
    'tp_subject.subjectconsent',
    version='1',
    start=edc_protocol.study_open_datetime,
    end=edc_protocol.study_close_datetime,
    age_min=18,
    age_max=60,
    gender=[MALE, FEMALE]
)

site_consents.register(v1)
