from django.shortcuts import render,HttpResponseRedirect
from tensorflow.python.eager.context import context
from .models import News
from django.views.generic import ListView,DetailView
from .src.predict import predict_class
from .forms import NewsForm

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


def PredictNews(request):
    # if this is a POST request we need to process the form data
    context={}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewsForm(request.POST)
        if form.is_valid():
            context['News'] = form.cleaned_data['query']
            context['label'] = predict_class(form.cleaned_data['query'])
    else:
        form = NewsForm()
    context['form'] = form
    return render(request, 'Predict.html',context)
