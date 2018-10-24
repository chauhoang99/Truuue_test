from django.conf.urls import url, include
from .views import ListCreateArticleView, SignupView, GetOrUpdateArticleByID, ListCreateCommentView, CustomLogoutView
from rest_framework_jwt.views import obtain_jwt_token
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^articles$', ListCreateArticleView.as_view(), name="list_articles"),
    url(r'^articles/(?P<pk>[-\w]+)$', GetOrUpdateArticleByID.as_view(), name="list_article"),
    url(r'^articles/(?P<article_id>[-\w]+)/comments$', ListCreateCommentView.as_view(), name="list_comment"),
    url(r'^login$', obtain_jwt_token, name='login'),
    url(r'^signup', SignupView.as_view(), name='sign_up'),
    url(r'^logout', csrf_exempt(CustomLogoutView.as_view()), name="logout")
]
