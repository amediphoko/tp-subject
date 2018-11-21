from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings


class AppConfig(DjangoAppConfig):
    name = 'tp_subject'
    verbose_name = 'Trainee Project Subject CRFs'
    admin_site_name = None  # edit after creating admin site

    def ready(self):
        from .models.signals import subject_consent_on_post_save


if settings.APP_NAME == 'tp_subject':

    from datetime import datetime
    from dateutil.relativedelta import (MO, TU, WE, TH, FR, SA, SU)
    from dateutil.tz.tz import gettz
    from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
    from edc_appointment.appointment_config import AppointmentConfig
    from edc_constants.constants import FAILED_ELIGIBILITY
    from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
    from edc_identifier.apps import AppConfig as BaseEdcIdentifierAppConfig
    from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
    from edc_lab.apps import AppConfig as BaseEdcLabAppConfig
    from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
    from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
    from edc_visit_tracking.constants import (
        SCHEDULED, UNSCHEDULED, LOST_VISIT, MISSED_VISIT)

    class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
        protocol = 'BHP092'
        protocol_number = '092'
        protocol_name = 'Trainee Project'
        protocol_title = 'TP'
        study_open_datetime = datetime(
            2016, 12, 31, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2018, 12, 31, 23, 59, 59, tzinfo=gettz('UTC'))

    class EdcIdentifierAppConfig(BaseEdcIdentifierAppConfig):
        identifier_prefix = '092'

    class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
        country = 'botswana'
        definitions = {
            '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                                 slots=[100, 100, 100, 100, 100, 100, 100]),
            '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                                 slots=[100, 100, 100, 100, 100])}

    class EdcLabAppConfig(BaseEdcLabAppConfig):
        base_template_name = 'trainee_project/base.html'
        requisition_model = 'tp_subject.subjectrequisition'
        result_model = 'edc_lab.result'

        @property
        def site_name(self):
            return 'Gaborone'

        @property
        def site_code(self):
            return '40'

    class EdcVisitingTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            'tp_subject': ('subject_visit', 'tp_subject.subjectvisit')}

    class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
        reason_field = {'tp_subject.subjectvisit': 'reason'}
        create_on_reasons = [SCHEDULED, UNSCHEDULED]
        delete_on_reasons = [LOST_VISIT, FAILED_ELIGIBILITY, MISSED_VISIT]

    class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
        default_appt_type = 'hospital'
        configurations = [
            AppointmentConfig(
                model='edc_appointment.appointment',
                related_visit_model='tp_subject.subjectvisit')
        ]
