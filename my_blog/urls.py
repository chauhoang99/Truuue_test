from django.conf.urls import url, include
from .views import ListCreateArticleView, SignupView, GetOrUpdateArticleByID, ListCreateCommentView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^articles$', ListCreateArticleView.as_view(), name="list_articles"),
    url(r'^articles/(?P<pk>[-\w]+)$', GetOrUpdateArticleByID.as_view(), name="list_article"),
    url(r'^articles/(?P<article_id>[-\w]+)/comments$', ListCreateCommentView.as_view(), name="list_comment"),
    url(r'^login$', obtain_jwt_token, name='create_token'),
    url(r'^signup', SignupView.as_view(), name='sign_up'),
]
