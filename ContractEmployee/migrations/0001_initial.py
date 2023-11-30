# Generated by Django 4.2.5 on 2023-10-19 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClEmpDet',
            fields=[
                ('cl_emp_code', models.IntegerField(primary_key=True, serialize=False)),
                ('cl_name', models.CharField(blank=True, max_length=25, null=True)),
                ('cl_work_locn', models.CharField(blank=True, max_length=25, null=True)),
                ('cl_edu_qual', models.CharField(blank=True, max_length=10, null=True)),
                ('cl_pre_addr1', models.CharField(blank=True, max_length=25, null=True)),
                ('cl_pre_addr2', models.CharField(blank=True, max_length=25, null=True)),
                ('cl_pre_addr3', models.CharField(blank=True, max_length=25, null=True)),
                ('cl_mob', models.CharField(blank=True, max_length=10, null=True)),
                ('cl_skill_typ', models.CharField(blank=True, max_length=15, null=True)),
                ('cl_act_hnd_by', models.CharField(blank=True, max_length=25, null=True)),
                ('cl_doj', models.DateField(blank=True, null=True)),
                ('cl_email', models.CharField(blank=True, max_length=25, null=True)),
                ('cl_adhar', models.CharField(blank=True, max_length=15, null=True)),
                ('cl_pan', models.CharField(blank=True, max_length=15, null=True)),
                ('cl_bnk_det', models.CharField(blank=True, max_length=25, null=True)),
                ('cl_per_addr1', models.CharField(blank=True, max_length=25, null=True)),
                ('cl_per_addr2', models.CharField(blank=True, max_length=25, null=True)),
                ('cl_per_addr3', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClVendorInfo',
            fields=[
                ('ven_code', models.BigIntegerField(primary_key=True, serialize=False)),
                ('ven_name', models.CharField(blank=True, max_length=25, null=True)),
                ('ven_addr1', models.CharField(blank=True, max_length=25, null=True)),
                ('ven_addr2', models.CharField(blank=True, max_length=25, null=True)),
                ('ven_addr3', models.CharField(blank=True, max_length=25, null=True)),
                ('ven_mob', models.IntegerField(blank=True, null=True)),
                ('ven_cont_prd', models.CharField(blank=True, max_length=25, null=True)),
                ('ven_adhar', models.BigIntegerField(blank=True, null=True)),
                ('ven_bank_det', models.CharField(blank=True, max_length=25, null=True)),
                ('ven_labr_reg', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClPayDet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cl_pay_basic', models.IntegerField(blank=True, null=True)),
                ('cl_allow', models.IntegerField(blank=True, null=True)),
                ('cl_bnk_det', models.CharField(blank=True, max_length=15, null=True)),
                ('cl_pay_emp_code', models.ForeignKey(blank=True, db_column='cl_pay_emp_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ContractEmployee.clempdet')),
            ],
        ),
        migrations.AddField(
            model_name='clempdet',
            name='cl_ven_code',
            field=models.ForeignKey(blank=True, db_column='cl_ven_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ContractEmployee.clvendorinfo'),
        ),
    ]
