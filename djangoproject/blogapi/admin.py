from django.contrib import admin
from blogapi.models import Posts, Comments, CommentsReply

# Register your models here.
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(CommentsReply)
