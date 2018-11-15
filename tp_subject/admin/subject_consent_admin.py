from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from ..forms import SubjectConsentForm
from ..models import SubjectConsent
from ..admin_site import tp_subject_admin


@admin.register(SubjectConsent, site=tp_subject_admin)
class SubjectConsentAdmin(admin.ModelAdmin):

    form = SubjectConsentForm

    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'subject_identifier',
                'first_name',
                'last_name',
                'initials',
                'language',
                'is_literate',
                'witness_name',
                'consent_datetime',
                'dob',
                'guardian_name',
                'is_dob_estimated',
                'identity',
                'identity_type',
                'confirm_identity',
                'is_incarcerated')}),
        ('Sample collection and storage', {
            'fields': (
                'may_store_samples',
                'may_store_genetic_samples')}),
        ('Review Questions', {
            'fields': (
                'consent_reviewed',
                'study_questions',
                'assessment_score',
                'consent_signature',
                'consent_copy'),
            'description': 'The following questions are directed to the interviewer.'}),
        audit_fieldset_tuple)

    search_fields = ['subject_identifier', 'screening_identifier', 'identity']

    radio_fields = {
        'assessment_score': admin.VERTICAL,
        'consent_copy': admin.VERTICAL,
        'consent_reviewed': admin.VERTICAL,
        'consent_signature': admin.VERTICAL,
        'gender': admin.VERTICAL,
        'is_dob_estimated': admin.VERTICAL,
        'is_incarcerated': admin.VERTICAL,
        'is_literate': admin.VERTICAL,
        'language': admin.VERTICAL,
        'may_store_genetic_samples': admin.VERTICAL,
        'may_store_samples': admin.VERTICAL,
        'study_questions': admin.VERTICAL, }
