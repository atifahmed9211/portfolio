from django.db import models

class blog(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateTimeField()
    text_body=models.TextField()
    post_image=models.ImageField(upload_to='images/')
