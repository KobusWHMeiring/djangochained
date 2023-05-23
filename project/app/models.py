from django.db import models

# Create your models here.

class Conversation(models.Model):
    user = models.CharField(max_length=100)
    message_title = models.CharField(max_length=200)
    message_content = models.TextField(max_length =20000)
    
    def __str__(self):
        return self.message_title
    
class Users(models.Model):
    name = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Tools(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name