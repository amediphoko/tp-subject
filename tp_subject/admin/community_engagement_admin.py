from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple, audit_fields
from ..admin_site import tp_subject_admin
from ..forms import CommunityEngagementForm
from ..models import CommunityEngagement


@admin.register(CommunityEngagement, site=tp_subject_admin)
class CommunityEngagementAdmin(admin.ModelAdmin):

    form = CommunityEngagementForm

    fieldset = (
        (None, {
            'fields': (
                'community_activity',
                'voted',
                'community_problems',
                'community_problems_other',
                'together_in_solving')}),
        audit_fieldset_tuple)

    radio_fields = {
        'community_activity': admin.VERTICAL,
        'voted': admin.VERTICAL,
        'community_problems': admin.VERTICAL,
        'together_in_solving': admin.VERTICAL
    }

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + audit_fields)
