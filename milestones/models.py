from django.db import models

# Create your models here.
class ProjectsTable(models.Model):
    project = models.CharField(max_length=128, unique=True)
    launch_date = models.DateField()

    def __str__(self):
        return self.project

class MilestonesTable(models.Model):
    STATUS_CHOICES = [('0', 'NOT_STARTED'), ('1', 'IN_PROGRESS'), ('2', 'COMPLETED'), ('3', 'BLOCKED')]

    milestone = models.CharField(max_length=128, unique=True)
    project = models.ForeignKey(ProjectsTable, on_delete=models.CASCADE)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NOT_STARTED')

    def __str__(self):
        return self.milestone
