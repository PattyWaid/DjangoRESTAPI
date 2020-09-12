from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blogapi.models import Posts, PostAuthorizer, Comments,CommentsReply
from django.db import models
from django.utils import timezone



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']




class CommentsSerializer(serializers.Serializer):
    commentid = serializers.ReadOnlyField()
    commenttext = serializers.CharField()
    commentuser = serializers.CharField()
    comments = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Posts.objects.all())
    comment_date = serializers.DateTimeField(read_only=True)
    commentreply = serializers.SerializerMethodField()


    def create(self, validated_data):
        comment = Comments(
            commenttext = validated_data['commenttext'],
            commentuser = validated_data['commentuser'],
            comments = validated_data['comments']
        )
        comment.save()
        return comment

    def get_commentreply(self, instance):
       commentReply = CommentsReply.objects.filter(commentreply=instance.commentid)
       print(commentReply)
       serializer = CommentsReplySerializer(commentReply, many=True)
       return serializer.data


class CommentsReplySerializer(serializers.Serializer):
    replytext = serializers.CharField(max_length=255)
    replyid = serializers.ReadOnlyField()
    replyuser = serializers.CharField()
    commentreply = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Comments.objects.all())
    reply_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        commentreply = CommentsReply(
            replytext=validated_data['replytext'],
            replyuser=validated_data['replyuser'],
            commentreply=validated_data['commentreply']
        )

        commentreply.save()
        return commentreply


class PostSerializer(serializers.Serializer):
    recid = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    imagepath = serializers.URLField()
    category = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=50)
    user = serializers.ReadOnlyField()
    date_created = serializers.DateTimeField(read_only=True)
    date_updated = serializers.DateTimeField(read_only=True)
    is_activated = serializers.BooleanField(read_only=True)
    activation_date = serializers.DateTimeField(read_only=True)
    authorization_status = serializers.CharField(read_only=True)
    authorizer = serializers.SerializerMethodField(read_only=True)
    comments = serializers.SerializerMethodField()
    listed = serializers.IntegerField(read_only=True)
    featured = serializers.IntegerField(read_only=True)


    def create(self, validated_data):
        print("Create Serializer Called", validated_data)

        post = Posts(
        name = validated_data['name'],
        description = validated_data['description'],
        imagepath = validated_data['imagepath'],
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
        instance.date_updated = timezone.now()
        instance.save()
        return instance


    def get_comments(self, instance):
       comments = Comments.objects.filter(comments=instance.recid)
       serializer = CommentsSerializer(comments, many=True)
       return serializer.data

    def get_authorizer(self, instance):
        print(instance.authorizer)
        authorizer_id = PostAuthorizer.objects.filter(authorizer_id=instance.authorizer_id)
        if authorizer_id:
            serializer = PostAuthorizerSerializer(authorizer_id, many=True)
            return serializer.data
        else:
            return []


class PostAuthorizerSerializer(serializers.Serializer):
    authorizer_id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=255)
    authorization_count = serializers.IntegerField()
    is_active = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        authorizer_data = PostAuthorizer(**validated_data)
        authorizer_data.save()
        return authorizer_data



