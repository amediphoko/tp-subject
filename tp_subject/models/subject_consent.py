from django.db import models
from django.apps import apps as django_apps
from edc_base.sites import SiteModelMixin
from edc_consent.model_mixins import ConsentModelMixin
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_consent.managers import ConsentManager
from edc_consent.field_mixins import (
    IdentityFieldsMixin, ReviewFieldsMixin, PersonalFieldsMixin)
from edc_consent.field_mixins import (
    VulnerabilityFieldsMixin, SampleCollectionFieldsMixin, CitizenFieldsMixin)
from edc_search.model_mixins import SearchSlugModelMixin, SearchSlugManager
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from ..managers import CurrentSiteManager
from edc_base.model_managers import HistoricalRecords


class SubjectConsentManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)


class SubjectConsent(ConsentModelMixin, SiteModelMixin, UpdatesOrCreatesRegistrationModelMixin,
                     NonUniqueSubjectIdentifierModelMixin, IdentityFieldsMixin, ReviewFieldsMixin,
                     PersonalFieldsMixin, SampleCollectionFieldsMixin, VulnerabilityFieldsMixin,
                     CitizenFieldsMixin, SearchSlugModelMixin, BaseUuidModel):

    participant_screening_model = 'tp_screening.participantscreening'

    screening_identifier = models.CharField(
        verbose_name='Screening Identifier',
        max_length=50)

    on_site = CurrentSiteManager()

    objects = SubjectConsentManager()

    consent = ConsentManager()

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.subject_identifier} V{self.version}'

    def save(self, *args, **kwargs):
        subject_screening = self.get_subject_screening()
        self.gender = subject_screening.gender
        self.subject_type = 'subject'
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.subject_identifier, self.version)

    def get_subject_screening(self):
        particpant_screening_cls = django_apps.get_model(
            self.participant_screening_model)
        return particpant_screening_cls.get(screening_identifier=self.screening_identifier)

    @property
    def registration_unique_field(self):
        return 'subject_identifier'

    class Meta(ConsentModelMixin.Meta):
        unique_together = (
            ('subject_identifier', 'version'),
            ('subject_identifier', 'screening_identifier'),
            ('first_name', 'dob', 'initials', 'version'))
