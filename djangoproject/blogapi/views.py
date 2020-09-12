from django.contrib.auth.models import User, Group
from rest_framework import status, viewsets
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from blogapi.serializers import (UserSerializer, GroupSerializer, PostSerializer, PostAuthorizerSerializer
 , CommentsSerializer, CommentsReplySerializer)
from blogapi.models import Posts, PostAuthorizer ,  Comments, CommentsReply
from django.http import JsonResponse
import json
from rest_framework.renderers import JSONRenderer
import pprint
from django.db.models import Q

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all().order_by('-date_joined')

def get_or_create(self, request):
    print("List:", self.request.data)
    print("RequestType =", request.method == 'POST')
    if (not request.method == 'POST'):
        print(request.data)
        print('Inside the GET Request')

        serializer = PostSerializer(self.queryset, many=True)
        pprint.pprint(json.dumps(serializer.data))
        return serializer.data
    else:
        print("This is a post request")
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data.values())
            serializer.save()
            return 200
        else:
            print(serializer.errors)
            return 400

class PostViewSet(viewsets.ViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


    def list(self, request):
         print("inside List", self.queryset)
         result = get_or_create(self, request)
         if(result):
             return Response(result)
         else:
             return Response("No Data Found")

    def retrieve(self, request, pk=None):
        print("PK", pk)
        if(pk == 'listed'):
            queryset = Posts.objects.filter(listed=1)
            serializer=PostSerializer(queryset, many=True)
            return Response(serializer.data)
        elif(pk == 'featured'):
            queryset = Posts.objects.filter(featured=1)
            serializer = PostSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = Posts.objects.get(pk=pk)
            serializer=PostSerializer(queryset)
            return Response(serializer.data)


    def create(self, request):
        print(request.data)
        result = get_or_create(self, request)
        print("Results",result)
        if (result == 200):
            print("Results", result)
            return Response({'status':'Created Successfully'})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        print("PK Update", pk)
        print("Request for Update", request.data)
        instance = self.queryset.get(pk=pk)
        serializer = PostSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        print("Inside Destroy")
        queryset = Posts.objects.all()
        print("PK", pk)
        instance = queryset.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class PostAuthorizerViewSet(viewsets.ViewSet):
    queryset = PostAuthorizer.objects.all()

    def list(self, request):
        serializer = PostAuthorizerSerializer(self.queryset, many=True)
        return Response(serializer.data)


class CommentsViewSet(viewsets.ViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def list(self, instance):
        serializer = CommentsSerializer(self.queryset, many=True)
        return Response(serializer.data)


    def create(self, request):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Created Successfully'})
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentsReplyViewSet(viewsets.ViewSet):
    queryset = CommentsReply.objects.all()
    serializer_class = CommentsReplySerializer

    def list(self, instance):
        serializer = CommentsReplySerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CommentsReplySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Created Successfully'})
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#
#
# class PostViewSet(viewsets.ViewSet):
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer
#
#     def list(self, request):
#         print("List")
#         queryset = Posts.objects.all()
#         serializer = PostSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         print("Retrieve")
#         print(pk)
#         queryset = Posts.objects.all()
#         post = get_object_or_404(queryset, pk=pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         print("Update")
#         queryset = Posts.objects.all()
#         instance = queryset.get(pk=pk)
#         serializer = PostSerializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def destroy(self, request, pk=None):
#         print("Destroy")
#         queryset = Posts.objects.all()
#         instance = queryset.get(pk=pk)
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class CreatePostViewSet(viewsets.ModelViewSet):
#     serializer_class = PostCreateSerializer
#     queryset = Posts.objects.all()
#
#     def create(self, request):
#         print("Create")
#         print(request.data)
#         serializer = PostCreateSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status': 'Created Successfully'})
#         else:
#             print(serializer.errors)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CommentsViewSet(viewsets.ModelViewSet):
#     queryset = Comments.objects.all()
#     serializer_class = CommentsSerializer
#
#

#
#
# class CommentsReplyViewSet(viewsets.ModelViewSet):
#     queryset = CommentsReply.objects.all()
#     serializer_class = CommentsReplySerializer
#
#
# class CreateCommentsReplyViewSet(viewsets.ModelViewSet):
#     queryset = CommentsReply.objects.all()
#     serializer_class = CreateCommentsReplySerializer
#
#     def create(self, request):
#         serializer = CreateCommentsReplySerializer(data=request.data.get('reply'))
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status': 'Created Successfully'})
#         else:
#             print(serializer.errors)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
