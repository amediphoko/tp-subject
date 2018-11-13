from django.db import models
from edc_constants.choices import YES_NO_NA_DWTA
from .model_mixins import CrfModelMixin
from ..custom_choices import ACTIVITY_LEVEL, PROBLEM_CHOICES


class CommunityEngagement(CrfModelMixin):
    '''Community Engagement Questionnaire'''

    community_activity = models.CharField(
        verbose_name="How active is the subject in community activities such"
                     " as Motshelo, Syndicate, PTA, VDC, Mophato & development"
                     " of the community that surrounds the subject?",
        max_length=20,
        choices=ACTIVITY_LEVEL,
        null=True,
        blank=True
    )

    voted = models.CharField(
        verbose_name="Did the subject vote during the last local government"
                     " election? ",
        max_length=15,
        choices=YES_NO_NA_DWTA,
        null=True,
        blank=True
    )

    community_problems = models.CharField(
        verbose_name="What are major problems in the neighbourhood? ",
        max_length=15,
        choices=PROBLEM_CHOICES,
        null=True,
        blank=True
    )

    community_problems_other = models.CharField(
        verbose_name="If other, please specify: ",
        max_length=50,
        null=True,
        blank=True
    )

    together_in_solving = models.CharField(
        verbose_name="If there is a problem in this neighbourhood, do "
                     "the adults work together in solving it? ",
        max_length=22,
        choices=YES_NO_NA_DWTA,
        null=True,
        blank=True
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'tp_subject'
        verbose_name = 'Community Engagement: Trainee Project'
        verbose_name_plural = 'Community Engagement: Trainee Project'
