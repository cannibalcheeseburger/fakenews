from django.urls import path
from news.views import HomeListView,NewsDetailView

#AgendaDetailView,

urlpatterns = [
    path('',HomeListView.as_view(),name = 'home'),
    path('news_detail/<int:pk>',NewsDetailView.as_view(),name = 'news_detail'),

]
