from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    quote = models.TextField()
    content = RichTextUploadingField(('content'))
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name='cate_blog')
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
