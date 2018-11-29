from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple, audit_fields
from ..admin_site import tp_subject_admin
from ..forms import EducationForm
from ..models import Education
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(Education, site=tp_subject_admin)
class EducationAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = EducationForm

    fieldset = (
        (None, {
            'fields': (
                'report_datetime',
                'subject_visit',
                'employment_status',
                'profession',
                'profession_other',
                'income_earnings')}),
        audit_fieldset_tuple)

    radio_fields = {
        'employment_status': admin.VERTICAL,
        'profession': admin.VERTICAL,
        'income_earnings': admin.VERTICAL}

    exclude = ('device_created', 'device_modified',)

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + audit_fields)
