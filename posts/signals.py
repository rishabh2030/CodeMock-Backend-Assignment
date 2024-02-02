import re
from django.conf import settings
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Paragraph)
def create_lead_creation(sender, instance, created, **kwargs):
    latest_paragraph = Paragraph.objects.latest('createdAt')

    if latest_paragraph:
        content_str = str(latest_paragraph.content)
        
        tokens = re.findall(r'\b\w+\b|\.', content_str)
        lowercase_tokens = map(str.lower, tokens)

        for token in lowercase_tokens:
            word_obj, created = Words.objects.get_or_create(word=token)
            word_obj.paragraph.add(latest_paragraph)