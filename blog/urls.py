#we're importing Django's function path and all of our views from the blog applicatio
from django.urls import path
from . import views

#our first url pattern
# assigning a view called post_list to the root URL.
#name='post_list', is the name of the URL that will be used to identify the view.
urlpatterns = [
    path('', views.post_list, name='post_list'),
]