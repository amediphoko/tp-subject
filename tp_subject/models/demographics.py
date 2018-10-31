from django.db import models
from ..custom_choices import MARITAL_STATUS_CHOICES, LIVING_ARRANGEMENTS


class Demographics():
    '''Demographics Questionnaire'''

    marital_status = models.CharField(
        verbose_name="What is the subject's marital"
                     " status?",
        max_length=8,
        choices=MARITAL_STATUS_CHOICES,
        null=True,
        blank=True)

    living_arr = models.CharField(
        verbose_name="Who does the subject currently live with?",
        max_length=30,
        choices=LIVING_ARRANGEMENTS,
        null=True,
        blank=True)

    number_of_spouses_f = models.IntegerField(
        verbose_name="How many wives does the subject's husband have"
                     "(including traditional marriage), including the subject?",
        null=True,
        blank=True,
    )

    number_of_spouses_m = models.IntegerField(
        verbose_name="How many wives does the subject have, including"
                     "traditional marriage?",
        null=True,
        blank=True
    )