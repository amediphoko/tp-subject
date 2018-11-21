import re

from django.test import TestCase
from edc_base.utils import get_utcnow
from edc_constants.constants import UUID_PATTERN
from edc_registration.models import RegisteredSubject
from model_mommy import mommy

from ..models import SubjectConsent


class TestSubjectConsent(TestCase):

    def setUp(self):
        self.subject_screening = mommy.make_recipe(
            'tp_screening.participantscreening')

    def test_allocated_subject_identifier(self):

        options = {
            'screening_identifier': self.subject_screening.screening_identifier,
            'consent_datetime': get_utcnow
        }
        mommy.make_recipe('tp_subject.subjectconsent', **options)
        self.assertFalse(
            re.match(UUID_PATTERN,
                     SubjectConsent.objects.all()[0].subject_identifier))

    def test_consent_creates_registered_subject(self):

        options = {
            'screening_identifier': self.subject_screening.screening_identifier,
            'consent_datetime': get_utcnow()
        }
        self.assertEquals(RegisteredSubject.objects.all().count(), 0)
        mommy.make_recipe('tp_subject.subjectconsent', **options)
        self.assertEquals(RegisteredSubject.objects.all().count(), 1)

#     def test_onschedule_created_on_consent(self):
#         subject_consent = mommy.make_recipe(
#             'tp_subject.subjectconsent',
#             consent_datetime=get_utcnow(),
#             screening_identifier=self.subject_screening.screening_identifier)
#         try:
#             OnSchedule.objects.get(
#                 subject_identifier=subject_consent.subject_identifier)
#         except ObjectDoesNotExist:
#             self.fail('ObjectDoesNotExist was unexpectedly raised.')
