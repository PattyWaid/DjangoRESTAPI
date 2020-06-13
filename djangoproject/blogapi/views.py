from django.contrib.auth.models import User, Group
from rest_framework import status,viewsets
from rest_framework.response import Response
from blogapi.serializers import UserSerializer, GroupSerializer, PostSerializer, CommentsSerializer, CommentsReplySerializer, PostCreateSerializer, CreateCommentsReplySerializer
from blogapi.models import Posts, Comments, CommentsReply


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer




class PostViewSet(viewsets.ModelViewSet): 

      serializer_class = PostSerializer
      queryset = Posts.objects.all()


# class PostByIdViewSet(viewsets.ModelViewSet):  

#       serializer_class = PostSerializer
#       queryset = Posts.objects.all()

#       def retrieve(self, request):
#             print(request.data)
#             post = get_object_or_404(queryset, pk=request.id)
#             serializer = PostSerializer(post)
#             return Response(serializer.data)

      
class CreatePostViewSet(viewsets.ModelViewSet):
    serializer_class = PostCreateSerializer
    queryset = Posts.objects.all()

    def create(self,request):
        serializer = PostCreateSerializer(data = request.data.get('post'))
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Created Successfully'})
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

      

class CommentsViewSet(viewsets.ModelViewSet):  

     queryset = Comments.objects.all()
     serializer_class = CommentsSerializer


class CreateCommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def create(self,request):
        serializer = CommentsSerializer(data = request.data.get('comments'))
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Created Successfully'})
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      

class CommentsReplyViewSet(viewsets.ModelViewSet):  
      queryset = CommentsReply.objects.all()
      serializer_class = CommentsReplySerializer


class CreateCommentsReplyViewSet(viewsets.ModelViewSet):
    queryset = CommentsReply.objects.all()
    serializer_class = CreateCommentsReplySerializer

    def create(self,request):
        serializer = CreateCommentsReplySerializer(data = request.data.get('reply'))

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Created Successfully'})
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    
      