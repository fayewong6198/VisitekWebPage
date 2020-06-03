from django.db import models
from datetime import datetime
from tinymce import HTMLField
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField('Content')
    category = models.CharField(max_length=255, default='Business')
    created_at = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    image = models.ImageField(upload_to='blog_images/')
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return self.image.url

    def get_url(self):
        return self.image.url

    def to_dict_url(self):
        return {"image": self.image.url}
