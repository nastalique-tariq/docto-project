from django.db import models

class DiseaseDoctorRelation(models.Model):
    
    disease = models.CharField( max_length=100)
    doctor = models.CharField( max_length=100)
    disease_description = models.TextField(max_length=2000)


    def __str__(self):
        return self.disease

# class Review(models.Model):
#     body = models.Textfield
    