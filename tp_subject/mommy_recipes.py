from dateutil.relativedelta import relativedelta
from django.contrib.sites.models import Site
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO, FEMALE
from faker import Faker
from model_mommy.recipe import Recipe, seq
from .models import SubjectConsent

fake = Faker()

subjectconsent = Recipe(
    SubjectConsent,
    assessment_score=YES,
    identity=seq('287125517'),
    confirm_identity=seq('287125517'),
    identity_type='country_id',
    consent_copy=YES,
    consent_datetime=get_utcnow(),
    consent_reviewed=YES,
    dob=get_utcnow() - relativedelta(years=22),
    first_name=fake.first_name,
    gender=FEMALE,
    initials='XX',
    is_dob_estimated='-',
    is_incarcerated=NO,
    is_literate=YES,
    last_name=fake.last_name,
    screening_identifier=None,
    study_questions=YES,
    site=Site.objects.get_current(),
    subject_identifier=None)
