from django.db import models
from django.utils import timezone
import datetime

AUTORIZATION_STATUS = (
    ('PENDING', 'Pending'),
    ('IN REVIEW', 'In Review'),
    ('COMPLETE', 'Complete')
)

CATEGORY = (
    ('TECHNOLOGY', 'Technology'),
    ('AUTOMOBILES', 'Automobiles'),
    ('ANIMATIONS', 'Animations'),
    ('DEFAULT', 'Unknown')
)
# Create your models here.\\
class PostAuthorizer(models.Model):
    authorizer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    authorization_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=0)

    def __str__(self):
        return self.name

class Posts(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    imagePath = models.URLField(blank=True)
    category = models.CharField(max_length=25, choices=CATEGORY, default='DEFAULT')
    email = models.EmailField(max_length=255, null=False)
   # comments = models.ForeignKey(to=Comments, on_delete=models.CASCADE, default=0)
    recId = models.AutoField(primary_key=True)
    user = models.CharField(max_length=20)
    date_created = models.DateTimeField(default=datetime.datetime.now)
    is_activated = models.BooleanField(null=True)
    activation_date = models.DateTimeField(blank=True, null=True)
    authorization_status = models.CharField(choices=AUTORIZATION_STATUS, default='PENDING', max_length=15)
    authorizer_id = models.ForeignKey(to=PostAuthorizer, null=True, blank=True,
                                      on_delete=models.SET_NULL)


    def __str__(self):
        return self.name

    def get_post_id(self):
        return self.recId


class Comments(models.Model):
    commentId = models.AutoField(primary_key=True)
    commentText = models.CharField(max_length=255)
    comments = models.ForeignKey(to=Posts, on_delete=models.CASCADE, default=0)
    #commentsReply = models.ForeignKey(to=CommentsReply, on_delete=models.CASCADE, default=0)
    commentUser = models.CharField(max_length=20)
    comment_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.commentText



class CommentsReply(models.Model):
    replyText = models.CharField(max_length=255)
    replyId = models.AutoField(primary_key=True)
    replyUser = models.CharField(max_length=20)
    commentReply = models.ForeignKey(to=Comments, on_delete=models.CASCADE, default=0)
    reply_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.replyText








    
























        





