from django.db import models

class symptom(models.Model):
  symptom = models.CharField(max_length=20)
  def __str__(self):
        return self.symptom

class treatment(models.Model):
    symptom = models.ForeignKey(symptom, on_delete=models.CASCADE)
    possible_diseases = models.TextField()
    treatment = models.TextField()

    def __str__(self):
        return self.treatment
# Create your models here.

class patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Non-binary', 'Non-binary'),
        ('Other', 'Other'),
    ]

    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Other')

    contact = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name