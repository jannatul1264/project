from . import views
from django.urls import path,re_path
urlpatterns = [
    path('',views.PostList.as_view(),name = 'home'),
    re_path('<slug:slug>/',views.PostList.as_view(),name='post_detail'),
        
]