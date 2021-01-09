from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    """Model definition for Post."""
    title = models.CharField(max_length=50)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    body = models.TextField(default=' ')

    # TODO: Define fields here


    def __str__(self):
        """Unicode representation of Post."""
        return self.author

    def get_absolute_url(self):
        # return reverse('snacks')
        return reverse('details_post', args=[str(self.id)])
