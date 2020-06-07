from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blogapi.models import Posts, Comments,CommentsReply


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']




class CommentsSerializer(serializers.ModelSerializer):
    commentReply = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = (
            'commentId', 'commentText', 'commentUser', 'comments', 'commentReply')

    def get_commentReply(self, instance):
       commentReply = CommentsReply.objects.all()
       serializer = CommentsReplySerializer(commentReply, many=True)
       return serializer.data
        
        

class CommentsReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentsReply
        fields = (
            'replyId', 'replyText', 'replyUser', 'commentReply'
        )
        

class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = (
            'recId', 'name', 'description', 'category', 'imagePath',
            'user', 'comments'
        )

    def get_comments(self, instance):
       comments = Comments.objects.all()
       serializer = CommentsSerializer(comments, many=True)
       return serializer.data

    
        