from django.db import models
import uuid
from users.models import Profile




class Athlete(models.Model):
    club = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="athlete-default.png")
    highlight_image = models.ImageField(
        null=True, blank=True, default=None)
    sponsors = models.ManyToManyField('Sponsor', blank=True)
    social_facebook = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    social_mail = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, 
                        editable=False)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url


class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, 
                        editable=False)
    
    def __str__(self):
        return self.name