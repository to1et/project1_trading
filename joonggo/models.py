from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sell(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject
    
class Comment(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()
    sell = models.ForeignKey(Sell, null=True, blank=True, on_delete=models.CASCADE)