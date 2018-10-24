from django.contrib import admin
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'admin/logout', admin.sites.AdminSite.logout, name='logout'),
    url(r'^api/auth/', include('my_blog.urls')),
]
