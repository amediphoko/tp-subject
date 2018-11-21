from tp_subject_validators.form_validators import CommunityEngagementFormValidator

from ..models import CommunityEngagement
from .form_mixins import SubjectModelFormMixin


class CommunityEngagementForm(SubjectModelFormMixin):

    form_validator_cls = CommunityEngagementFormValidator

    class Meta:
        model = CommunityEngagement
        fields = '__all__'
