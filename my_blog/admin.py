from django.contrib import admin
from my_blog.models import Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'author_key_id')
    search_fields = ['id', 'author', 'title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'comment')
