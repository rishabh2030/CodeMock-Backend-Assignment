from rest_framework import serializers
from .models import Paragraph,Words

class ParagraphSerializer(serializers.ModelSerializer):
    """
    Serializer for the Paragraph model.

    Serializes the Paragraph model fields for use in API views.
    """
    class Meta:
        model = Paragraph
        fields = ['id', 'user', 'content']

class WordsSerializer(serializers.ModelSerializer):
    """
    Serializer for the Words model.

    Serializes the Words model fields for use in API views.

    Includes a nested serialization of the related Paragraphs using ParagraphSerializer.
    """
    paragraph = ParagraphSerializer(many=True, read_only=True)

    class Meta:
        model = Words
        fields = ['paragraph']