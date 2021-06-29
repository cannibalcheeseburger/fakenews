from news.views import HomeListView,NewsDetailView
from django.urls import path,include
#AgendaDetailView,

urlpatterns = [
    path('',HomeListView.as_view(),name = 'home'),
    path('news_detail/<int:pk>',NewsDetailView.as_view(),name = 'news_detail'),

]
