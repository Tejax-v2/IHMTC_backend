from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Participant(models.Model):
    HONORIFIC_CHOICES = [
        ('Prof.', 'Prof.'),
        ('Dr.', 'Dr.'),
        ('Mr.', 'Mr.'),
        ('Ms.', 'Ms.'),
    ]
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    NUM_PAPERS_CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
    ]
    CATEGORY_CHOICES = [
        ('Student', 'I am a Student'),
        ('Faculty', 'I am a Faculty'),
        ('Others', 'I am affiliated with industry/research labs/others'),
    ]
    NUM_ACCOMPANYING_CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
    ]
    ISHMT_MEMBER_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    AFFILIATION_COUNTRY = [
        ('SAARC', 'SAARC'),
        ('Non-SAARC','Non-SAARC'),
    ]
    email = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    honorific = models.CharField(max_length=10, choices=HONORIFIC_CHOICES,blank=True,null=True)
    full_name = models.CharField(max_length=100,blank=True,null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,blank=True,null=True)
    birth_year = models.PositiveIntegerField(blank=True, null=True)
    affiliation = models.CharField(max_length=100,blank=True,null=True)
    country_of_affiliation = models.CharField(max_length=10, choices=AFFILIATION_COUNTRY,blank=True,null=True)
    country_code = models.CharField(max_length=5,blank=True,null=True)
    contact_number = models.CharField(max_length=20,blank=True,null=True)
    whatsapp_country_code = models.CharField(max_length=5,blank=True,null=True)
    whatsapp_contact_number = models.CharField(max_length=20,blank=True,null=True)
    num_papers = models.CharField(max_length=2, choices=NUM_PAPERS_CHOICES,blank=True,null=True)
    paper1_id = models.CharField(max_length=50,blank=True,null=True)
    paper2_id = models.CharField(max_length=50,blank=True,null=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES,blank=True,null=True)
    num_accompanying_people = models.CharField(max_length=2, choices=NUM_ACCOMPANYING_CHOICES,blank=True,null=True)
    is_ishmt_member = models.CharField(max_length=3, choices=ISHMT_MEMBER_CHOICES,blank=True,null=True)
    ishmt_id = models.CharField(max_length=100,blank=True,null=True)
    ishmt_id_file = models.FileField(upload_to='ishmt_ids/',blank=True,null=True)
    forgot_pass_token = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.full_name
