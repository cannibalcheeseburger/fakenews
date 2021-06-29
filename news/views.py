from django.shortcuts import render
from .models import News
from django.views.generic import ListView,DetailView

# Create your views here.
class HomeListView(ListView):
    model = News
    template_name = 'home.html'
    context_object_name = 'news'
    queryset = News.objects.order_by('-date')[:15]
    
class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'