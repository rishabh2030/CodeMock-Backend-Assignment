from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Paragraph,Words
from .serializers import ParagraphSerializer,WordsSerializer
from rest_framework.permissions import IsAuthenticated
from helper.functions import ResponseHandling
from helper import messages, keys
from helper.functions import *
from rest_framework.filters import SearchFilter

class ArticleCreateView(generics.CreateAPIView):
    """
    API endpoint for creating an article.

    Inherits from generics.CreateAPIView to handle article creation.

    Requires authentication for access (IsAuthenticated permission).
    """
    permission_classes = [IsAuthenticated]
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer

    def create(self, request, *args, **kwargs):
        """
        Handle the creation of an article.

        :param request: The HTTP request object containing the article data.
        :param args: Additional arguments.
        :param kwargs: Additional keyword arguments.
        :return: Response containing the result of the article creation.
        """
        try :
            article = request.body.decode('utf-8')
            paragraphs = article.split('\r\n\r\n')
            user = request.user
            for paragraph in paragraphs:
                Paragraph.objects.create(user=user, content=paragraph)
            return Response(ResponseHandling.success_response_message(messages.ARTICLE_POSTED,messages.OPERATION_SUCCESS),status=status201)
        except Exception as e:
            return Response(ResponseHandling.failure_response_message(messages.SOMETHING_WRONG,messages.OPERATION_FAILED),status=status500)
        

class WordSearchView(generics.ListAPIView):
    """
    API endpoint for searching and retrieving paragraphs containing a specific word.

    Inherits from generics.ListAPIView to handle listing paragraphs.

    Requires authentication for access (IsAuthenticated permission).
    """
    serializer_class = ParagraphSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request, *args, **kwargs):
        """
        Handle the search and retrieval of paragraphs containing a specific word.

        :param request: The HTTP request object containing the word query parameter.
        :param args: Additional arguments.
        :param kwargs: Additional keyword arguments.
        :return: Response containing the paragraphs matching the word.
        """
        word = self.request.query_params.get('word', None).lower()
        if word:
            try:
                word_instance = Words.objects.get(word=word)
                paragraphs = word_instance.paragraph.all()[:10]
                serializer = self.get_serializer(paragraphs, many=True)

                return Response (serializer.data)
            except Words.DoesNotExist:
                return Response (ResponseHandling.failure_response_message(messages.WORD_DOES_NOT_EXIST,messages.OPERATION_FAILED),status=status404)
        else:
            return Response(ResponseHandling.failure_response_message(messages.ENTER_WORD,messages.OPERATION_FAILED),status=status404)
            
