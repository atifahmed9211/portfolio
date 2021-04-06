from django.db import models

class blog(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateTimeField()
    text_body=models.TextField()
    post_image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.text_body[:100] # is tah ue text_body ke first 100 character return karta ha.
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %y') # to modify DATE, IF WE WANT TO SHOW ONLY DATE
