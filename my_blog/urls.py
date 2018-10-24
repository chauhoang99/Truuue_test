from django.conf.urls import url, include
from .views import ListCreateArticleView, SignupView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^articles$', ListCreateArticleView.as_view(), name="list_articles"),
    url(r'^login$', obtain_jwt_token, name='create_token'),
    url(r'^signup', SignupView.as_view(), name='sign_up'),
]
