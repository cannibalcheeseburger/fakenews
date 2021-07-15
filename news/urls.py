from news.views import HomeListView,NewsDetailView, news_create
from news.views import loginView,registerView,logoutUser,user_article,self_article,news_create
from django.urls import path,include


urlpatterns = [
    path('',HomeListView.as_view(),name = 'home'),
    path('news_detail/<int:pk>',NewsDetailView.as_view(),name = 'news_detail'),
    path('login/', loginView, name='login'),
    path('register/', registerView, name='register'),
    path('logout/',logoutUser, name='logout'),
    path('user/', self_article, name='user'),
    path('user/<str:username>', user_article, name='user_article'),
    path('form/', news_create, name='newscreate')

]
