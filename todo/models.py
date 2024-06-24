from django.db import models

# Create your models here.


class Todo(models.Model):

    PRIORITY=(
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low'),
    )
  
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    priority = models.PositiveIntegerField(choices=PRIORITY, default=3)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
