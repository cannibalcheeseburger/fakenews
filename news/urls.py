from news.views import HomeListView,NewsDetailView,loginView,registerView,logoutUser,UserListView
from django.urls import path,include


urlpatterns = [
    path('',HomeListView.as_view(),name = 'home'),
    path('news_detail/<int:pk>',NewsDetailView.as_view(),name = 'news_detail'),
    path('login/', loginView, name='login'),
    path('register/', registerView, name='register'),
    path('logout/',logoutUser, name='logout'),
    path('user/', UserListView.as_view(), name='user'),

]
