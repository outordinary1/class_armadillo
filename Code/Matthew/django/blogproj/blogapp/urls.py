
from django.urls import path
from . import views

app_name = 'blogapp'
urlpatterns = [
    # localhost:8000/
    path('', views.index, name='index'),
    # localhost:8000/5/
    # localhost:8000/23/
    path('<int:blog_post_id>/', views.detail, name='detail'),
    path('new/', views.create_post_page, name='create_post_page'),
    path('save_post/', views.save_post, name='save_post'),
]