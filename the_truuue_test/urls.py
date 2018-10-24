from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.views import login
from rest_framework.authtoken import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'admin/logout', admin.sites.AdminSite.logout, name='logout'),
    url(r'^api/auth/', include('my_blog.urls')),
    url(r'^$', login, name='login')
]
