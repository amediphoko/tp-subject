from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from .subject_consent import SubjectConsent


@receiver(post_save, weak=False, sender=SubjectConsent,
          dispatch_uid='subject_consent_on_post_save')
def subject_consent_on_post_save(sender, instance, raw, created, **kwargs):
    if not raw:
        if not created:
            _, schedule = site_visit_schedules.get_by_onschedule_model(
                'tp_subject.onschedule')
            schedule.refresh_schedule(
                subject_identifier=instance.subject_identifier)
        else:
            subject_screening = 