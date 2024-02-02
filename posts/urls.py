from django.urls import path
from .views import *

urlpatterns = [
    path('post/add_article/', ArticleCreateView.as_view(), name='post article'),
    path('words/search/', WordSearchView.as_view(), name='search_word'),
]