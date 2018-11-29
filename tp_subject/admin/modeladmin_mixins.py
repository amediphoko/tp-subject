from django.contrib import admin
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_model_admin import ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin
from edc_model_admin import ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin
from edc_model_admin import ModelAdminRedirectOnDeleteMixin, ModelAdminReadOnlyMixin
from edc_model_admin import ModelAdminInstitutionMixin
from edc_metadata.next_form_getter import NextFormGetter
from edc_visit_tracking.modeladmin_mixins import CrfModelAdminMixin as VisitTrackingCrfModelAdminMixin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_fieldsets.fieldsets_modeladmin_mixin import FieldsetsModelAdminMixin
from edc_model_admin.form_as_json_model_admin_mixin import FormAsJSONModelAdminMixin


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin, ModelAdminRedirectOnDeleteMixin,
                      ModelAdminSiteMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'
    next_form_getter_cls = NextFormGetter


class CrfModelAdminMixin(VisitTrackingCrfModelAdminMixin,
                         ModelAdminMixin,
                         FieldsetsModelAdminMixin,
                         FormAsJSONModelAdminMixin,
                         admin.ModelAdmin):
    show_save_next = True
    show_cancel = True
