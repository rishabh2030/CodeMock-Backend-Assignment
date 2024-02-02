from django.db import models
from helper.models import BaseModel
from django.contrib.auth import get_user_model
Users = get_user_model()


class Paragraph(BaseModel):
    """
    Model representing paragraphs.

    Inherits from BaseModel for common features.

    Each paragraph belongs to a user and contains textual content.
    """
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        ordering = ['createdAt']

    def __str__(self):
        return f'{self.user.name} - {self.content[:50]}'
    

class Words(BaseModel):
    """
    Model representing individual words.

    Inherits from BaseUserModel for user-specific features.

    Each word has a unique word value and is associated with multiple paragraphs.
    """
    word = models.CharField(max_length=100, unique=True)
    paragraph = models.ManyToManyField(Paragraph, related_name='paragraphs') 

    def __str__(self):
        return self.word