from .form_mixins import SubjectModelFormMixin
from ..models import CommunityEngagement
from ..form_validators import CommunityEngagementFormValidator


class CommunityEngagementForm(SubjectModelFormMixin):

    form_validator_cls = CommunityEngagementFormValidator

    class Meta:
        model = CommunityEngagement
        fields = '__all__'
