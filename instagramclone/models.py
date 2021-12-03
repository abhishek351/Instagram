from django.db import models
from django.contrib.auth.models import User
import PIL.Image as Image
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="post_user")
    photo=models.ImageField(upload_to="media")
    caption=models.CharField(max_length=150,default='')
    datetime=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User,blank=True,related_name='likes')
    
    

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.photo.path)
        width, height = img.size  

        if height < width:
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))

        elif width < height:
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))

        img.save(self.photo.path)


    def __str__(self):
        return f'{self.user.username}: {self.caption[:15]}...'

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="profilepic",default='default.jpg')
    website = models.URLField(default='', blank=True)
    bio = models.TextField(default='', blank=True)
    followers=models.ManyToManyField(User,blank=True,related_name="followers")

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.photo.path)
        width, height = img.size  # Get dimensions

        if width > 300 and height > 300:
            # keep ratio but shrink down
            img.thumbnail((width, height))

        # check which one is smaller
        if height < width:
            # make square by cutting off equal amounts left and right
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))

        elif width < height:
            # make square by cutting off bottom
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))

        if width > 300 and height > 300:
            img.thumbnail((300, 300))

        img.save(self.photo.path)


    def __str__(self):
        return f'{self.user.username}'

    
@receiver(post_save, sender=User) #add this
def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile.objects.create(user=instance)

@receiver(post_save, sender=User) #add this
def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()



class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(post,on_delete=models.CASCADE,related_name="comments")
    comment = models.TextField()
    datetime=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username}\'s comment on "{self.post.caption[:15]}..." post: {self.comment}' 



class Notification(models.Model):
    #1-like,2-comment,3-follow
    notification_type=models.IntegerField()
    from_user=models.ForeignKey(User,related_name="notification_from",on_delete=models.CASCADE,null=True)
    to_user=models.ForeignKey(User,related_name="notification_to",on_delete=models.CASCADE,null=True)
    posts=models.ForeignKey('post',on_delete=models.CASCADE,related_name="+",null=True,blank=True)
    comment=models.ForeignKey('Comment',on_delete=models.CASCADE,related_name="+",null=True,blank=True)
    date=models.DateTimeField(default=timezone.now)
    user_has_seen=models.BooleanField(default=False)
