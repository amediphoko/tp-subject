from django.db import models
from edc_constants.choices import YES_NO_NA_DWTA
from ..custom_choices import ACTIVITY_LEVEL


class CommunityEngagement():
    '''Community Engagement Questionnaire'''

    community_activity = models.CharField(
        verbose_name="How active is the subject in community activities such"
                     " as Motshelo, Syndicate, PTA, VDC, Mophato & development"
                     " of the community that surrounds the subject?",
        max_length=20,
        choices=ACTIVITY_LEVEL,
        null=True,
        blank=True)

    voted = models.CharField(
        verbose_name="Did the subject vote during the last local government"
                     " election?",
        max_length=15,
        choices=YES_NO_NA_DWTA,
        null=True,
        blank=True)