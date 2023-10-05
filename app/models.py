from django.db import models
from django.db.models import CharField,ImageField,OneToOneField,CASCADE, DateTimeField,ForeignKey
from django.contrib.auth.models import User
import json
class BlogPost(models.Model):
    image = ImageField(upload_to='post_images')
    title = CharField(max_length=1000)
    text = CharField(max_length=100000) # will be a list containing multiple paragraphs
    author = ForeignKey(User,on_delete=CASCADE)
    date_created = DateTimeField(auto_now_add=True)

    def get_paragraphs(self):
        return json.loads(self.text)
    
    def get_some_words(self):
        paragraphs = self.get_paragraphs()
        if paragraphs:
            first = paragraphs[0]
            few_words = ' '.join(first.split()[:20])
            return few_words


class Comment(models.Model):
    text = CharField(max_length=1000)
    post = ForeignKey(BlogPost,on_delete=CASCADE)
    user = ForeignKey(User,on_delete=CASCADE)

class ImageProfile(models.Model):
    user = OneToOneField(User,on_delete=CASCADE)
    image = ImageField(upload_to='profile_images')
# Create your models here.
