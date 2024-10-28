from django.db import models


# Create your models here.
class robo(models.Model):
    username = models.CharField(max_length=100)
    like = models.IntegerField()
    comment = models.IntegerField()
    share = models.IntegerField()
    about = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    
    class Meta:
        db_table = "posts"
    