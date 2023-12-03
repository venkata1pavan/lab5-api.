from rest_framework.views import APIView
from rest_framework.response import Response 

from posts import models
from .serializers import postserializers

class PublicPostList (APIView):
    """"""
    Return the most public recent post by all users   
    """"""
    def get (self, request):
        msgs = models.post.objects.public_posts () [:5]
        data = postserializers(msgs, many =True).data
        return Response(data)