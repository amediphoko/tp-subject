from .form_mixins import SubjectModelFormMixin
from ..models import Education


class EducationForm(SubjectModelFormMixin):

    # formvalidaotorhere

    class Meta:
        model = Education
        fields = '__all__'
