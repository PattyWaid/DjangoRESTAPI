from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blogapi.models import Posts, Comments,CommentsReply, PostAuthorizer
from django.db import models
import json



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']




class CommentsSerializer(serializers.Serializer):
    commentId = serializers.ReadOnlyField()
    commentText = serializers.CharField()
    commentUser = serializers.CharField()
    comments = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Posts.objects.all())
    comment_date = serializers.DateTimeField(read_only=True)
    commentReply = serializers.SerializerMethodField()


    def create(self, validated_data):
        comment = Comments(
            commentText = validated_data['commentText'],
            commentUser = validated_data['commentUser'],
            comments = validated_data['comments']
        )
        comment.save()
        return comment





    def get_commentReply(self, instance):
       commentReply = CommentsReply.objects.filter(commentReply=instance.commentId)
       serializer = CommentsReplySerializer(commentReply, many=True)
       return serializer.data

        
        

class CommentsReplySerializer(serializers.Serializer):
    replyText = serializers.CharField(max_length=255)
    replyId = serializers.ReadOnlyField()
    replyUser = serializers.CharField()
    commentReply = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Comments.objects.all())
    reply_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        commentreply = CommentsReply(
            replyText=validated_data['replyText'],
            replyUser=validated_data['replyUser'],
            commentReply=validated_data['commentReply']
        )

        commentreply.save()
        return commentreply
        

class PostSerializer(serializers.Serializer):
    recId = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    imagePath = serializers.URLField()
    category = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=50)
    user = serializers.ReadOnlyField()
    date_created = serializers.DateTimeField(read_only=True)
    is_activated = serializers.BooleanField(read_only=True)
    activation_date = serializers.DateTimeField(read_only=True)
    authorization_status = serializers.CharField(read_only=True)
    authorizer_id = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()



    def create(self, validated_data):
        print("Create Serializer Called", validated_data)

        post = Posts(
        name = validated_data['name'],
        description = validated_data['description'],
        imagePath = validated_data['imagePath'],
        category = validated_data['category'],
        email = validated_data['email'],
        user = validated_data['email'].split('@')[0],
        #is_activated = validated_data['is_activated'],
        )

        post.save()
        return post

    def update(self, instance, validated_data):
        print("Instance",instance)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


    def get_comments(self, instance):
       comments = Comments.objects.filter(comments=instance.recId)
       serializer = CommentsSerializer(comments, many=True)
       return serializer.data

    def get_authorizer_id(self, instance):
        print(instance.authorizer_id)
        authorizer_id = PostAuthorizer.objects.filter(authorizer_id=instance.authorizer_id_id)
        serializer = PostAuthorizerSerializer(authorizer_id, many=True)
        return serializer.data


class PostAuthorizerSerializer(serializers.Serializer):
    authorizer_id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=255)
    authorization_count = serializers.IntegerField()
    is_active = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        authorizer_data = PostAuthorizer(**validated_data)
        authorizer_data.save()
        return authorizer_data



