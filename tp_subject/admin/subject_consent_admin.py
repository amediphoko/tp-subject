from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch
from edc_model_admin import (ModelAdminNextUrlRedirectMixin,
                             ModelAdminFormAutoNumberMixin,
                             ModelAdminInstitutionMixin,
                             ModelAdminReplaceLabelTextMixin,
                             ModelAdminNextUrlRedirectError)
from edc_model_admin import audit_fieldset_tuple
from edc_model_admin.model_admin_audit_fields_mixin import audit_fields
from ..forms import SubjectConsentForm
from ..models import SubjectConsent
from ..admin_site import tp_subject_admin


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin, ModelAdminFormAutoNumberMixin,
                      ModelAdminRevisionMixin, ModelAdminReplaceLabelTextMixin,
                      ModelAdminInstitutionMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'

    def redirect_url(self, request, obj, post_url_continue=None):
        redirect_url = super().redirect_url(
            request, obj, post_url_continue=post_url_continue)
        if request.GET.dict().get('next'):
            url_name = request.GET.dict().get('next').split(',')[0]
            attrs = request.GET.dict().get('next').split(',')[1:]
            options = {k: request.GET.dict().get(k)
                       for k in attrs if request.GET.dict().get(k)}
            options.update(subject_identifier=obj.subject_identifier)
            try:
                redirect_url = reverse(url_name, kwargs=options)
            except NoReverseMatch as e:
                raise ModelAdminNextUrlRedirectError(
                    f'{e}. Got url_name={url_name}, kwargs={options}.')
        return redirect_url


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

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + audit_fields)
