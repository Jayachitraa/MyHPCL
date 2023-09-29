from django.db import models

class Contractemphpcl(models.Model):
    QUALIFICATION_CHOICES = [
        ('skilled', 'Skilled'),
        ('unskilled', 'Unskilled'),
        ('semiskilled', 'Semi Skilled'),
        ('highly_skilled', 'Highly Skilled'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    ]
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    quali = models.CharField(max_length=20,choices=QUALIFICATION_CHOICES,blank=True,null=True)
    
    org_name = models.CharField(max_length=100, blank=True, null=True)
    desg = models.CharField(max_length=50, blank=True, null=True)
    ven_code = models.CharField(max_length=20, blank=True, null=True)
    basic = models.CharField(max_length=20, blank=True, null=True)
    doj = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES,blank=True,null=True)
    
    add1 = models.CharField(max_length=100, blank=True, null=True)
    add2 = models.CharField(max_length=100, blank=True, null=True)
    pin = models.CharField(max_length=100, blank=True, null=True)
    mob = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    esic_enrolled = models.CharField(max_length=20, blank=True, null=True)
    esic_location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Contractemphpcl'