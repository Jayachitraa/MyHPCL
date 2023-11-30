# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ClEmpDet(models.Model):
    cl_ven_code = models.ForeignKey('ClVendorInfo', models.DO_NOTHING, db_column='cl_ven_code', blank=True, null=True)
    cl_emp_code = models.IntegerField(primary_key=True)
    cl_name = models.CharField(max_length=25, blank=True, null=True)
    cl_work_locn = models.CharField(max_length=25, blank=True, null=True)
    cl_edu_qual = models.CharField(max_length=10, blank=True, null=True)
    cl_pre_addr1 = models.CharField(max_length=25, blank=True, null=True)
    cl_pre_addr2 = models.CharField(max_length=25, blank=True, null=True)
    cl_pre_addr3 = models.CharField(max_length=25, blank=True, null=True)
    cl_mob = models.CharField(max_length=10, blank=True, null=True)
    cl_skill_typ = models.CharField(max_length=15, blank=True, null=True)
    cl_act_hnd_by = models.CharField(max_length=25, blank=True, null=True)
    cl_doj = models.DateField(blank=True, null=True)
    cl_email = models.CharField(max_length=25, blank=True, null=True)
    cl_adhar = models.CharField(max_length=15, blank=True, null=True)
    cl_pan = models.CharField(max_length=15, blank=True, null=True)
    cl_bnk_det = models.CharField(max_length=25, blank=True, null=True)
    cl_per_addr1 = models.CharField(max_length=25, blank=True, null=True)
    cl_per_addr2 = models.CharField(max_length=25, blank=True, null=True)
    cl_per_addr3 = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cl_emp_det'


class ClPayDet(models.Model):
    cl_pay_emp_code = models.ForeignKey(ClEmpDet, models.DO_NOTHING, db_column='cl_pay_emp_code', blank=True, null=True)
    cl_pay_basic = models.IntegerField(blank=True, null=True)
    cl_allow = models.IntegerField(blank=True, null=True)
    cl_bnk_det = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cl_pay_det'


class ClVendorInfo(models.Model):
    ven_code = models.BigIntegerField(primary_key=True)
    ven_name = models.CharField(max_length=25, blank=True, null=True)
    ven_addr1 = models.CharField(max_length=25, blank=True, null=True)
    ven_addr2 = models.CharField(max_length=25, blank=True, null=True)
    ven_addr3 = models.CharField(max_length=25, blank=True, null=True)
    ven_mob = models.IntegerField(blank=True, null=True)
    ven_cont_prd = models.CharField(max_length=25, blank=True, null=True)
    ven_adhar = models.BigIntegerField(blank=True, null=True)
    ven_bank_det = models.CharField(max_length=25, blank=True, null=True)
    ven_labr_reg = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cl_vendor_info'
