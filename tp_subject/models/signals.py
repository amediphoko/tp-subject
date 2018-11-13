from django.core.exceptions import ValidationError
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save, post_delete
from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from tp_screening.models import SubjectScreening
from .subject_consent import SubjectConsent
from .subject_visit import SubjectVisit


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
            # update identifier and consented
            subject_screening = SubjectScreening.objects.get(
                screening_identifier=instance.screening_identifier)
            subject_screening.subject_identifer = instance.subject_identifier
            subject_screening.consented = True
            subject_screening.save_base(
                update_fields=['subject_identifier', 'consented'])

            # put subject on schedule
            _, schedule = site_visit_schedules.get_by_onschedule_model(
                'tp_subject.onschedule')
            schedule.put_on_schedule(
                subject_identifier=instance.subject_identifier,
                onschedule_datetime=instance.consent_datetime)

            # create or delete action for re-consent


@receiver(post_delete, weak=False, sender=SubjectConsent,
          dispatch_uid='subject_consent_on_post_delete')
def subject_consent_on_post_delete(sender, instance, using, **kwargs):
    """Updates or resets subject screening."""
    # don't allow if visits exists. This should be caught in the
    # ModelAdmin delete view
    if SubjectVisit.objects.filter(subject_identifier=instance.subject_identifier).exists():
        raise ValidationError('Unable to delete consent. Visit data exists.')

    _, schedule = site_visit_schedules.get_by_onschedule_model(
        'tp_subject.onschedule')
    schedule.take_off_schedule(
        subject_identifier=instance.subject_identifier,
        offschedule_datetime=instance.consent_datetime)

    # update subject screening
    subject_screening = SubjectScreening.objects.get(
        screening_identifier=instance.screening_identifier)
    subject_screening.consented = False
    subject_screening.subject_identifier = subject_screening.subject_screening_as_pk
    subject_screening.save()
