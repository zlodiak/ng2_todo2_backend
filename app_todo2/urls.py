from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^users_list$', views.users_list, name='users_list'),
  
  url(r'^create_todo$', views.create_todo, name='create_todo'),
  url(r'^create_todo2$', views.create_todo2, name='create_todo2'),
  url(r'^get_todos$', views.get_todos, name='get_todos'),
  url(r'^update_todo$', views.update_todo, name='update_todo'),
  url(r'^update_todos$', views.update_todos, name='update_todos'),
  url(r'^remove_todo$', views.remove_todo, name='remove_todo'),
  url(r'^remove_todos_completed$', views.remove_todos_completed, name='remove_todos_completed'),

  url(r'^create_marker$', views.create_marker, name='create_marker'),
]
