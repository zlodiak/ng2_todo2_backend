from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
  # Examples:
  # url(r'^$', 'todo2.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),

  url(r'^admin/', include(admin.site.urls)),
  url(r'app_todo2/', include('app_todo2.urls')),
]
