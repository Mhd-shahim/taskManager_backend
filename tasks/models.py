from django.db import models
from datetime import date


# Create your models here.
class tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')
    due_date = models.DateField()
    created_at = models.DateField(default=date.today)

    def __str__(self):
        return self.title