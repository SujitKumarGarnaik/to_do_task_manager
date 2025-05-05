from django.db import models
from django.utils import timezone

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    STATUS_CHOICES = [
        ('N', 'Not Started'),
        ('I', 'In Progress'),
        ('C', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES,default='M')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-priority','due_date']