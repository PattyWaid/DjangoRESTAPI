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


class Comments(models.Model):
    commentid = models.AutoField(db_column='commentId', primary_key=True)  # Field name made lowercase.
    commenttext = models.CharField(db_column='commentText', max_length=255)  # Field name made lowercase.
    comments = models.ForeignKey('Posts', models.DO_NOTHING, db_column='comments', blank=True, null=True)
    commentuser = models.CharField(db_column='commentUser', max_length=25)  # Field name made lowercase.
    comment_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comments'


class Commentsreply(models.Model):
    replyid = models.AutoField(db_column='replyId', primary_key=True)  # Field name made lowercase.
    replytext = models.CharField(db_column='replyText', max_length=255)  # Field name made lowercase.
    replyuser = models.CharField(db_column='replyUser', max_length=255)  # Field name made lowercase.
    commentreply = models.IntegerField(db_column='commentReply')  # Field name made lowercase.
    reply_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'commentsreply'


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


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField(blank=True, null=True)
    is_activated = models.IntegerField(blank=True, null=True)
    activation_date = models.DateTimeField(blank=True, null=True)
    authorization_status = models.CharField(max_length=50)
    authorizer = models.ForeignKey(PostAuthorizer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'
