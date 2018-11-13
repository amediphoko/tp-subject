from django.db import models
from edc_constants.choices import YES_NO
from .model_mixins import EducationModelMixin, CrfModelMixin
from ..custom_choices import WORK_TYPE_CHOICES, INCOME_SCALE


class Education(EducationModelMixin, CrfModelMixin):
    '''Education Questionnaire'''

    employment_status = models.CharField(
        verbose_name="Is the subject currently employed?",
        max_length=3,
        choices=YES_NO,
        null=True,
        blank=True)

    profession = models.CharField(
        verbose_name="What is your profession?",
        max_length=30,
        choices=WORK_TYPE_CHOICES,
        null=True,
        blank=True)

    profession_other = models.CharField(
        verbose_name="If other, please specify: ",
        max_length=50,
        null=True,
        blank=True)

    income_earnings = models.CharField(
        verbose_name="What is the subject's income scale?",
        max_length=10,
        choices=INCOME_SCALE,
        null=True,
        blank=True
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'tp_subject'
        verbose_name = 'Education: Trainee Program'
        verbose_name_plural = 'Education: Trainee Program'
