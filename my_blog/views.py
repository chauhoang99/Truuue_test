
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions, generics
from rest_framework.views import status


# Get the JWT settings, add these lines after the import/from lines
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginView(generics.CreateAPIView):
    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class ListCreateArticleView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        author = self.request.query_params.get('author')
        page = self.request.query_params.get('page')

        if page and author:
            paginator = Paginator(Article.objects.filter(author=author), 10)
            try:
                queryset = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                queryset = paginator.page(page)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                page = paginator.num_pages
                queryset = paginator.page(page)
        elif page:
            paginator = Paginator(Article.objects.all(), 10)
            try:
                queryset = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                queryset = paginator.page(page)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                page = paginator.num_pages
                queryset = paginator.page(page)
        elif author:
            queryset = Article.objects.filter(author=author)
        else:
            queryset = Article.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        article = Article.objects.create(
            title=request.data["title"],
            author=request.data["author"],
            content=request.data["content"]
        )
        return Response(
            data=ArticleSerializer(article).data,
            status=status.HTTP_201_CREATED
        )


class SignupView(generics.CreateAPIView):
    model = User
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
