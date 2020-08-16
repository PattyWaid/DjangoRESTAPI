from django.contrib import admin
from blogapi.models import Posts, Comments, CommentsReply, PostAuthorizer

# Register your models here.
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(CommentsReply)
admin.site.register(PostAuthorizer)
