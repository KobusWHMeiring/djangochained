from django.db import models

# Create your models here.

class Conversation(models.Model):
    user = models.CharField(max_length=200, default=None, blank=True)  
    date_time = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length = 2000, default=None, blank=True)
    message_title = models.CharField(max_length = 200, default=None, blank=True)
    
    def __str__(self):
        return self.message

    def get_most_recent_message(cls):
        most_recent_message = cls.objects.latest('date_time')
        return most_recent_message
    
    
class Additional(models.Model):
    item = models.CharField(max_length = 200)
    link = models.ForeignKey(Conversation, on_delete=models.CASCADE)