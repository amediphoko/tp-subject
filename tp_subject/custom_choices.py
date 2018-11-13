from edc_constants.constants import NOT_APPLICABLE
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, MISSED_VISIT


NA = 'NOT ANSWERING'
OT = 'OTHER'


MARITAL_STATUS_CHOICES = (
    ('SINGLE', 'Single'),
    ('MARRIED', 'Married'),
    ('DIVORCED', 'Divorced'),
    ('WIDOWED', 'Widowed'),)

LIVING_ARRANGEMENTS = (
    ('ALONE', 'Alone'),
    ('PARTNER', 'Partner'),
    ('SIBLINGS', 'Siblings'),
    ('OTHER', 'Other'),
    (NA, 'Don\'t want to answer'),)

WORK_TYPE_CHOICES = (
    ('CASUAL EMPLOYMENT', 'Casual Employment'),
    ('SEASONAL EMPLOYMENT', 'Seasonal Employment'),
    ('FW FULL TIME', 'Formal Wage (Full-Time)'),
    ('FW PART TIME', 'Formal Wage (Part-Time)'),
    ('SE AGRICULTURE', 'Self Employed in Agriculture'),
    ('SE FULL TIME', 'Self Employed Full Time'),
    ('SE PART TIME', 'Self Employed Part Time'),
    (NA, 'Don\'t want to answer'),
    (OT, 'Other'),)

INCOME_SCALE = (
    ('None', 'No income'),
    ('1-199', '1-199 pula'),
    ('200-499', '200-499 pula'),
    ('500-999', '500-999 pula'),
    ('1000-4999', '1000-4999 pula'),
    ('5000-10000', '5000-10000 pula'),
    ('>10000', 'More than 10000 pula'),
    (NA, 'Don\'t want to answer'))

ACTIVITY_LEVEL = (
    ('VERY', 'Very Active'),
    ('SOMEWHAT', 'Somewhat Active'),
    ('NOT ACTIVE', 'Not active'),
    (NA, 'Don\'t want to answer'),)

PROBLEM_CHOICES = (
    ('HIV/AIDS', 'HIV and AIDS'),
    ('SCHOOLS', 'Schools'),
    ('SEWER', 'Sewer'),
    ('UNEMPLOYMENT', 'Unemployment'),
    ('ROADS', 'Roads'),
    ('WATER', 'Water'),
    (OT, 'Other'),
    ('HOUSE', 'House'),
    ('MALARIA', 'Malaria'),)

ID_TYPE = (
    ('country_id', 'Country ID number'),
    ('drivers', 'Driver\'s license'),
    ('passport', 'Passport'),
    ('hospital_no', 'Hospital number'),
    ('country_id_rcpt', 'Country ID receipt'),
    (OT, 'Other'),)

INFO_SOURCE = (
    ('hospital_notes', 'Hospital notes'),
    ('outpatient_cards', 'Outpatient cards'),
    ('patient', 'Patient'),
    ('collateral_history',
     'Collateral History from relative/guardian'),
    (OT, 'Other'),
)

VISIT_UNSCHEDULED_REASON = (
    ('patient_unwell_outpatient', 'Patient unwell (outpatient)'),
    ('recurrence_symptoms', 'Recurrence of symptoms'),
    ('raised_icp_management', 'Raised ICP management'),
    ('art_initiation', 'ART initiation'),
    ('patient_hospitalised', 'Patient hospitalised'),
    (OT, 'Other'),
    (NOT_APPLICABLE, 'Not applicable'),
)


VISIT_REASON = (
    (SCHEDULED, 'Scheduled'),
    (UNSCHEDULED, 'Not scheduled'),
    (MISSED_VISIT, 'Missed'),
)
