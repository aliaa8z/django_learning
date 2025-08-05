from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'posts')
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)

    # model meta option
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.slug} - {self.updated}"

    def get_absolute_url(self):
	    return reverse('home:post_detail', args=(self.id, self.slug))

    def likes_count(self):
        return self.plike.count()

    def user_can_like(self, user):
        user_like = user.ulike.filter(post= self)
        if user_like.exists():
            return True
        return False


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'ucomment')
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name= 'pcomment')
    reply = models.ForeignKey('self', on_delete= models.CASCADE, related_name= 'rcomment', blank= True, null= True)
    is_reply = models.BooleanField(default = False)
    body = models.TextField(max_length= 300)
    created = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.user} - {self.body[:30]}"


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'ulike')
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name= 'plike')

    def __str__(self):
        return f"{self.user} likes {self.post.slug}"