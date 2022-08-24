from django.db import models

# Create your models here.
class SendMail(models.Model):
    subject = models.CharField(max_length=100)
    useremail = models.EmailField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.subject