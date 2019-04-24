from django.db import models  
from django.urls import reverse  
from django.contrib.auth.models import User  

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename) 
  
class Funds(models.Model):  
  

  
   user = models.ForeignKey(User, on_delete=models.CASCADE)  
   title = models.CharField(max_length=200)  
   description = models.CharField(max_length=2000000)
   amount_to_be_collected = models.CharField(max_length=200)  
   collected_amount = models.CharField(max_length=200)
   upload = models.FileField(upload_to='images/')
   
   
  
   def __unicode__(self):  
     return self.title  
  
   def get_absolute_url(self):  
     return reverse('CRUD_FBVs:movies_edit', kwargs={'pk': self.pk})  
