#we're importing Django's function path and all of our views from the blog applicatio
from django.urls import path
from . import views

#our first url pattern
# assigning a view called post_list to the root URL.
#name='post_list', is the name of the URL that will be used to identify the view.
urlpatterns = [
    path('', views.post_list, name='post_list'),
    #post/ means that the URL should begin with the word post followed by a /. 
    #int pk means that Django expects an integer value and will transfer it to a view as a variable called pk.

    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]