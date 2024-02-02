from rest_framework import serializers
from .models import Paragraph

class ParagraphSerializer(serializers.Serializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'user', 'content']
        