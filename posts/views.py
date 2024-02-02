# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Paragraph
from .serializers import ParagraphSerializer
from rest_framework.permissions import IsAuthenticated
from helper.functions import ResponseHandling
from helper import messages, keys
from helper.functions import *

class ArticleCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer

    def create(self, request, *args, **kwargs):
        try :
            article = request.body.decode('utf-8')
            paragraphs = article.split('\r\n\r\n')
            user = request.user
            for paragraph in paragraphs:
                Paragraph.objects.create(user=user, content=paragraph)
            return Response(ResponseHandling.success_response_message(messages.ARTICLE_POSTED,messages.OPERATION_SUCCESS),status=status201)
        except Exception as e:
            return Response(ResponseHandling.failure_response_message(messages.SOMETHING_WRONG,messages.OPERATION_FAILED),status=status500)