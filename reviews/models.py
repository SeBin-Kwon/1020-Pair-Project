from django.db import models

# Create your models here.

class Review(models.Model):
    user = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    content = models.TextField()
    movie_name = models.CharField(max_length=20)
    grade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to='images/', blank=True)
    
class Comment(models.Model):
    reivew = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.CharField(max_length=20)
    content = models.CharField(max_length=80)