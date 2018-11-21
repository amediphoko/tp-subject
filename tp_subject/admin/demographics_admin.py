from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple, audit_fields
from ..admin_site import tp_subject_admin
from ..forms import DemographicsForm
from ..models import Demographics


@admin.register(Demographics, site=tp_subject_admin)
class DemographicsAdmin(admin.ModelAdmin):

    form = DemographicsForm

    fieldset = (
        (None, {
            'fields': (
                'marital_status',
                'living_arr',
                'number_of_spouses_f',
                'number_of_spouses_m')}),
        audit_fieldset_tuple)

    radio_fields = {
        'marital_status': admin.VERTICAL,
        'living_arr': admin.VERTICAL,
    }

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + audit_fields)
