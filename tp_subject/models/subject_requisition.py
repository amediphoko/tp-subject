from edc_lab.models import (
    RequisitionModelMixin, RequisitionIdentifierMixin, RequisitionStatusMixin)


class SubjectRequisition(RequisitionModelMixin, RequisitionStatusMixin,
                         RequisitionIdentifierMixin):
    pass
