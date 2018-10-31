from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from django.db import models
from edc_constants.choices import YES_NO
from .model_mixins import EducationModelMixin
from ..custom_choices import WORK_TYPE_CHOICES, INCOME_SCALE


class Education(EducationModelMixin):
    '''Education Questionnaire'''

    employment_status = models.CharField(
        verbose_name="Is the subject currently employed?",
        max_length=3,
        choices=YES_NO,
        null=True,
        blank=True)

    work_type = models.CharField(
        verbose_name="What type of work does the subject do?",
        max_length=30,
        choices=WORK_TYPE_CHOICES,
        null=True,
        blank=True)

    income_earnings = models.CharField(
        verbose_name="In the past month, how much money did the subject"
                     " earn from the work they did or received in payment?",
        max_length=10,
        choices=INCOME_SCALE,
        null=True,
        blank=True
    )
