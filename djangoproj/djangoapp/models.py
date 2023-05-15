from django.db import models

# Create your models here.

class Conversation(models.Model):
    user = models.CharField(max_length=200)  
    date_time = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length = 2000)
    
    def __str__(self):
        return self.message

    @classmethod
    def get_most_recent_message(cls):
        most_recent_message = cls.objects.latest('date_time')
        return most_recent_message
    
    
    