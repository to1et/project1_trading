from django.db import models
# from django.contrib.auth.models import User
from common.models import User

# Create your models here.

class Sell(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_sell')

    subject = models.CharField(max_length=200)
    content = models.TextField()
    images = models.ImageField(blank=True, upload_to='images')
    category = models.TextField(default="") # 카테고리
    price = models.IntegerField(default=0) # 가격
    tmethod = models.TextField(default="") # 거래 방식
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    voter = models.ManyToManyField(User, related_name='voter_sell')

    def __str__(self):
        return self.subject
    
class Comment(models.Model):
    sell = models.ForeignKey(Sell, null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)