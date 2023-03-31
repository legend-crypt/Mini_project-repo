from django.db import models
from django.contrib.auth  import get_user_model

# Create your models here.
User = get_user_model()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    

class Description(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')

    
    def __str__(self):
        return f"{self.name}"
    