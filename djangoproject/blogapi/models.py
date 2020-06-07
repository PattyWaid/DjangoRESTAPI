from django.db import models

# Create your models here.\\

class Posts(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    imagePath = models.URLField(blank=True)
    category = models.CharField(max_length=255)
   # comments = models.ForeignKey(to=Comments, on_delete=models.CASCADE, default=0)
    recId = models.AutoField(primary_key=True)
    user = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Comments(models.Model):
    commentId = models.AutoField(primary_key=True)
    commentText = models.CharField(max_length=255)
    comments = models.ForeignKey(to=Posts, on_delete=models.CASCADE, default=0)
    #commentsReply = models.ForeignKey(to=CommentsReply, on_delete=models.CASCADE, default=0)
    commentUser = models.CharField(max_length=10)

    def __str__(self):
        return self.commentText



class CommentsReply(models.Model):
    replyText = models.CharField(max_length=255)
    replyId = models.AutoField(primary_key=True)
    replyUser = models.CharField(max_length=10)
    commentReply = models.ForeignKey(to=Comments, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.replyText




    
























        





