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
# This is with sqlite DB

# Create your models here.\\
# class PostAuthorizer(models.Model):
#     authorizer_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255, null=False)
#     authorization_count = models.IntegerField(default=0)
#     is_active = models.BooleanField(default=0)
#
#     def __str__(self):
#         return self.name
#
# class Posts(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     imagePath = models.URLField(blank=True)
#     category = models.CharField(max_length=25, choices=CATEGORY, default='DEFAULT')
#     email = models.EmailField(max_length=255, null=False)
#    # comments = models.ForeignKey(to=Comments, on_delete=models.CASCADE, default=0)
#     recId = models.AutoField(primary_key=True)
#     user = models.CharField(max_length=20)
#     date_created = models.DateTimeField(default=timezone.now)
#     date_updated = models.DateTimeField(blank=True, null=True)
#     is_activated = models.BooleanField(null=True)
#     activation_date = models.DateTimeField(blank=True, null=True)
#     authorization_status = models.CharField(choices=AUTORIZATION_STATUS, default='PENDING', max_length=15)
#     authorizer_id = models.ForeignKey(to=PostAuthorizer, null=True, blank=True,
#                                       on_delete=models.SET_NULL)
#
#
#     def __str__(self):
#         return self.name
#
#     def get_post_id(self):
#         return self.recId


# class Comments(models.Model):
#     commentId = models.AutoField(primary_key=True)
#     commentText = models.CharField(max_length=255)
#     comments = models.ForeignKey(to=Posts, on_delete=models.CASCADE, default=0)
#     #commentsReply = models.ForeignKey(to=CommentsReply, on_delete=models.CASCADE, default=0)
#     commentUser = models.CharField(max_length=20)
#     comment_date = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return self.commentText
#
#
#
# class CommentsReply(models.Model):
#     replyText = models.CharField(max_length=255)
#     replyId = models.AutoField(primary_key=True)
#     replyUser = models.CharField(max_length=20)
#     commentReply = models.ForeignKey(to=Comments, on_delete=models.CASCADE, default=0)
#     reply_date = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#         return self.replyText


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogapiComments(models.Model):
    commentid = models.AutoField(db_column='commentId', primary_key=True)  # Field name made lowercase.
    commenttext = models.CharField(db_column='commentText', max_length=255)  # Field name made lowercase.
    commentuser = models.CharField(db_column='commentUser', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'blogapi_comments'


class BlogapiCommentsreply(models.Model):
    replytext = models.CharField(db_column='replyText', max_length=255)  # Field name made lowercase.
    replyid = models.AutoField(db_column='replyId', primary_key=True)  # Field name made lowercase.
    replyuser = models.CharField(db_column='replyUser', max_length=10)  # Field name made lowercase.
    commentreply_id = models.IntegerField(db_column='commentReply_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'blogapi_commentsreply'


class BlogapiPosts(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    imagepath = models.CharField(db_column='imagePath', max_length=200)  # Field name made lowercase.
    category = models.CharField(max_length=255)
    recid = models.AutoField(db_column='recId', primary_key=True)  # Field name made lowercase.
    user = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'blogapi_posts'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class PostAuthorizer(models.Model):
    authorizer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    authorization_count = models.IntegerField()
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'post_authorizer'


class Posts(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    imagepath = models.CharField(db_column='imagePath', max_length=255)  # Field name made lowercase.
    category = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    recid = models.AutoField(db_column='recId', primary_key=True)  # Field name made lowercase.
    user = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(null=True)
    is_activated = models.BooleanField(null=True, default=0)
    activation_date = models.DateTimeField(blank=True, null=True)
    authorization_status = models.CharField(choices=AUTORIZATION_STATUS, default='PENDING', max_length=15)
    authorizer = models.ForeignKey(PostAuthorizer, models.DO_NOTHING, null=True)
    listed = models.IntegerField(default=0)
    featured = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'posts'


class Comments(models.Model):
    commentid = models.AutoField(db_column='commentId', primary_key=True)  # Field name made lowercase.
    commenttext = models.CharField(db_column='commentText', max_length=255)  # Field name made lowercase.
    comments = models.ForeignKey(Posts, models.DO_NOTHING, db_column='comments', blank=True, null=True)
    commentuser = models.CharField(db_column='commentUser', max_length=255)  # Field name made lowercase.
    comment_date = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'comments'


class CommentsReply(models.Model):
    replyid = models.AutoField(db_column='replyId', primary_key=True)  # Field name made lowercase.
    replytext = models.CharField(db_column='replyText', max_length=255)  # Field name made lowercase.
    replyuser = models.CharField(db_column='replyUser', max_length=255)  # Field name made lowercase.
    commentreply = models.ForeignKey(Comments, models.DO_NOTHING,db_column='commentReply', null=True)  # Field name made lowercase.
    reply_date = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'commentsreply'


    
























        





