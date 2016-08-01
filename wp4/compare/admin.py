#!/usr/bin/python
# coding: utf-8
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from django.utils import timezone
# from reversion_compare.admin import CompareVersionAdmin
from reversion.admin import VersionAdmin

# Register your models here.
from .models import OrganPerson, RetrievalTeam, Donor, Recipient, Organ
from .models import ProcurementResource, OrganAllocation, Randomisation


# CORE Admin classes used throughout the whole system
class BaseModelAdmin(admin.ModelAdmin):
    exclude = ('created_on', 'created_by')
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True
    date_hierarchy = 'created_on'

    def save_model(self, request, obj, form, change):
        obj.save(created_by=request.user)

    def save_formset(self, request, form, formset, change):
        """
        Need to override the standard save_formset to ensure that the user is added to created_by

        :param request:
        :param form:
        :param formset:
        :param change:
        :return:
        """
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.save(created_by=request.user)
        formset.save_m2m()


class VersionControlAdmin(VersionAdmin):
    exclude = ('version', 'created_on', 'created_by', 'record_locked')
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True
    date_hierarchy = 'created_on'

    def save_model(self, request, obj, form, change):
        obj.save(created_by=request.user)

    def save_formset(self, request, form, formset, change):
        """
        Need to override the standard save_formset to ensure that the user is added to created_by

        :param request:
        :param form:
        :param formset:
        :param change:
        :return:
        """
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.save(created_by=request.user)
        formset.save_m2m()


# Compare Admin modules
class RetrievalTeamAdmin(VersionAdmin):
    list_display = ('based_at', 'centre_code')
    ordering = ('centre_code',)
    fields = ('centre_code', 'based_at')

    def save_model(self, request, obj, form, change):
        obj.save(created_by=request.user)

admin.site.register(RetrievalTeam, RetrievalTeamAdmin)


class OrganPersonAdmin(VersionControlAdmin):
    list_display = ('__str__', 'number', 'gender', 'age_from_dob',  'date_of_death', 'recipient', 'donor')
    ordering = ('id',)
    fields = (
        'number',
        'date_of_birth',
        'date_of_birth_unknown',
        'date_of_death',
        'date_of_death_unknown',
        'gender',
        'weight',
        'height',
        'ethnicity',
        'blood_group'
    )

admin.site.register(OrganPerson, OrganPersonAdmin)


class DonorAdmin(VersionControlAdmin):
    list_display = (
        '__str__',
        'person',
        'retrieval_team',
        'perfusion_technician',
        'is_randomised',
    )
    list_per_page = 20
    list_select_related = ('retrieval_team', 'perfusion_technician', 'person')
    ordering = ('retrieval_team', 'sequence_number')
    fieldsets = [
        ('Case information', {'fields': [
            'sequence_number',
            'multiple_recipients',
            'not_randomised_because',
            'not_randomised_because_other',
            'procurement_form_completed',
            'admin_notes'
        ]}),
        ('Trial Procedure', {'fields': [
            'retrieval_team',
            'perfusion_technician',
            'transplant_coordinator',
            'call_received',
            'call_received_unknown',
            'retrieval_hospital',
            'scheduled_start',
            'scheduled_start_unknown',
            'technician_arrival',
            'technician_arrival_unknown',
            'ice_boxes_filled',
            'ice_boxes_filled_unknown',
            'depart_perfusion_centre',
            'depart_perfusion_centre_unknown',
            'arrival_at_donor_hospital',
            'arrival_at_donor_hospital_unknown'
        ]}),
        ('Donor Details', {'fields': [
            'person',
            'age',
            'date_of_admission',
            'date_of_admission_unknown',
            'admitted_to_itu',
            'date_admitted_to_itu',
            'date_admitted_to_itu_unknown',
            'date_of_procurement',
            'other_organs_procured',
            'other_organs_lungs',
            'other_organs_pancreas',
            'other_organs_liver',
            'other_organs_tissue'
        ]}),
        ('PreOp Data', {'fields': [
            'diagnosis',
            'diagnosis_other',
            'diabetes_melitus',
            'alcohol_abuse',
            'cardiac_arrest',
            'systolic_blood_pressure',
            'diastolic_blood_pressure',
            'diuresis_last_day',
            'diuresis_last_day_unknown',
            'diuresis_last_hour',
            'diuresis_last_hour_unknown',
            'dopamine',
            'dobutamine',
            'nor_adrenaline',
            'vasopressine',
            'other_medication_details'
        ]}),
        ('Lab Results', {'fields': [
            'last_creatinine',
            'last_creatinine_unit',
            'max_creatinine',
            'max_creatinine_unit'
        ]}),
        ('Operation Data', {'fields': [
            'life_support_withdrawal',
            'systolic_pressure_low',
            'systolic_pressure_low_unknown',
            'o2_saturation',
            'o2_saturation_unknown',
            'circulatory_arrest',
            'circulatory_arrest_unknown',
            'length_of_no_touch',
            'death_diagnosed',
            'perfusion_started',
            'perfusion_started_unknown',
            'systemic_flush_used',
            'systemic_flush_used_other',
            'systemic_flush_volume_used',
            'heparin'
        ]}),
    ]

admin.site.register(Donor, DonorAdmin)


class OrganAllocationAdmin(VersionControlAdmin):
    ordering = ('organ__pk', 'created_on')
    list_display = (
        '__str__', 'organ', 'perfusion_technician', 'transplant_hospital',
        'reallocated', 'reallocation'
    )
    fields = (
        'organ',
        'perfusion_technician',
        'call_received',
        'call_received_unknown',
        'transplant_hospital',
        'theatre_contact',
        'scheduled_start',
        'scheduled_start_unknown',
        'technician_arrival',
        'technician_arrival_unknown',
        'depart_perfusion_centre',
        'depart_perfusion_centre_unknown',
        'arrival_at_recipient_hospital',
        'arrival_at_recipient_hospital_unknown',
        'journey_remarks',
        'reallocated',
        'reallocation_reason',
        'reallocation_reason_other',
        'reallocation'
    )

admin.site.register(OrganAllocation, OrganAllocationAdmin)


class ProcurementResourceInline(admin.TabularInline):
    model = ProcurementResource
    fields = ('type', 'lot_number', 'expiry_date', 'expiry_date_unknown')
    can_delete = True
    extra = 0


class OrganAllocationInline(admin.StackedInline):
    model = OrganAllocation
    fields = OrganAllocationAdmin.fields   # Hacky?
    can_delete = False
    extra = 0


class OrganAdmin(VersionControlAdmin):
    list_display = (
        '__str__', 'location', 'transplantable', 'donor', 'is_allocated', 'explain_is_allocated',
        'reallocation_count', 'transplantation_form_completed'
    )
    ordering = ('donor__retrieval_team', 'donor__sequence_number', 'location')
    fieldsets = [
        ('Context', {'fields': [
            'donor',
            'location',
        ]}),
        ('Transplantation Form metadata', {'fields': [
            'admin_notes',
            'not_allocated_reason',
            'transplantation_form_completed',
            'transplantation_notes',
        ]}),
        ('Inspection', {'fields': [
            'removal',
            'renal_arteries',
            'graft_damage',
            'graft_damage_other',
            'washout_perfusion',
            'transplantable',
            'not_transplantable_reason'
        ]}),
        ('Randomisation', {'fields': [
            'preservation'
        ]}),
        ('Perfusion', {'fields': [
            'perfusion_possible',
            'perfusion_not_possible_because',
            'perfusion_started',
            'patch_holder',
            'artificial_patch_used',
            'artificial_patch_size',
            'artificial_patch_number',
            'oxygen_bottle_full',
            'oxygen_bottle_open',
            'oxygen_bottle_changed',
            'oxygen_bottle_changed_at',
            'oxygen_bottle_changed_at_unknown',
            'ice_container_replenished',
            'ice_container_replenished_at',
            'ice_container_replenished_at_unknown',
            'perfusate_measurable',
            'perfusate_measure',
            'perfusion_machine',
            'perfusion_file'
        ]})
    ]
    inlines = [
        ProcurementResourceInline,
        OrganAllocationInline
    ]

    def save_formset(self, request, form, formset, change):
        if formset.model == ProcurementResource:
            for subform in formset:
                subform.instance.created_by = request.user
                subform.instance.created_on = timezone.now()
            formset.save()
        else:
            super(OrganAdmin, self).save_formset(request, form, formset, change)

admin.site.register(Organ, OrganAdmin)


class RecipientAdmin(VersionControlAdmin):
    list_display = (
        '__str__', 'person', 'organ', 'allocation', 'signed_consent', 'successful_conclusion'
    )
    ordering = ('organ__pk', 'created_on')
    fieldsets = [
        ('Case information', {'fields': [
            'person',
            'organ',
            'allocation',
            'signed_consent',
            'single_kidney_transplant',
        ]}),
        ('Recipient Details', {'fields': [
            'renal_disease',
            'renal_disease_other',
            'pre_transplant_diuresis',
        ]}),
        ('Peri-operative data', {'fields': [
            'knife_to_skin',
            'perfusate_measure',
            'perfusion_stopped',
            'organ_cold_stored',
            'tape_broken',
            'removed_from_machine_at',
            'oxygen_full_and_open',
            'organ_untransplantable',
            'organ_untransplantable_reason',
            'anesthesia_started_at',
            'incision',
            'transplant_side',
            'arterial_problems',
            'arterial_problems_other',
            'venous_problems',
            'venous_problems_other',
            'anastomosis_started_at',
            'anastomosis_started_at_unknown',
            'reperfusion_started_at',
            'reperfusion_started_at_unknown',
            'mannitol_used',
            'other_diurectics',
            'other_diurectics_details',
            'systolic_blood_pressure',
            'cvp',
            'intra_operative_diuresis',
            'successful_conclusion',
            'operation_concluded_at',
        ]}),
        ('Machine cleanup record', {'fields': [
            'probe_cleaned',
            'ice_removed',
            'oxygen_flow_stopped',
            'oxygen_bottle_removed',
            'box_cleaned',
            'batteries_charged',
            'cleaning_log'
        ]}),
    ]

admin.site.register(Recipient, RecipientAdmin)


class RandomisationAdmin(VersionAdmin):
    list_display = ('id', 'list_code', 'donor', 'result', 'allocated_on')
    ordering = ('id',)
    fields = ('donor', 'result', 'allocated_on')

admin.site.register(Randomisation, RandomisationAdmin)
