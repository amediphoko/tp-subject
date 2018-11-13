from .form_mixins import SubjectModelFormMixin
from ..models import Demographics
from ..form_validators import DemographicsFormValidator


class DemographicsForm(SubjectModelFormMixin):

    form_validator_cls = DemographicsFormValidator

    class Meta:
        model = Demographics
        fields = '__all__'
