"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from blogapi import views
from rest_framework import routers

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet,'posts-list')
# router.register(r'comments', views.CommentsViewSet)
router.register(r'create', views.PostViewSet, 'create-list')
# router.register(r'reply', views.CommentsReplyViewSet)
router.register(r'add/comments', views.CommentsViewSet)
router.register(r'add/reply', views.CommentsReplyViewSet)
router.register(r'posts/<int:recId>', views.PostViewSet, 'post-update')
router.register(r'posts/<int:recId>', views.PostViewSet, 'post-detail')
router.register(r'posts/<int:recId>', views.PostViewSet, 'post-delete')
router.register(r'authorizers', views.PostAuthorizerViewSet, 'authorizers_list')




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    #path('posts/', PostViewSet),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path(r'^api-auth/', include('rest_framework.urls'))
# ]
