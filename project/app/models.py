from django.db import models
import uuid

# Create your models here.

class Conversation(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    guid = models.UUIDField(primary_key = True,
         default = uuid.uuid4,
         editable = False)
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    
class Messages(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    prompt_value = models.TextField()
    system_value = models.TextField()
    role = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.prompt_value