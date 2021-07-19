from tensorflow.python.eager.context import context
from .models import News
from .src.predict import predict_class
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView,DetailView
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,NewsForm,NewNewsForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

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

    
def loginView(request):
    context= {}
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,"Username or Password is incorrect")
            return render(request, 'login.html', context)
    return render(request,'login.html',context)

def registerView(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"Accout Created Successfully")
            return redirect('login')
    context= {'form':form}
    return render(request,'register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def self_article(request):
    username  =str(request.user.username)
    news = News.objects.filter(author=username)
    return render(request,'userdetail.html',{'News':news})

def user_article(request,username):
    news = News.objects.filter(author=username)
    return render(request,'user_articles.html',{'News':news,'username':username})



def news_create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewNewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            label = predict_class(text)
            author = str(request.user.username)
            article = News(title=title,text=text,author=author,label=label)
            article.save()
            return redirect('user')

    form = NewNewsForm()
    return render(request, 'news_form.html',{'form':form})


def del_article(request,id):
    if request.user.is_authenticated:
        article = News.objects.get(id = id)
        if request.user.username == article.author:
        #additional check
            article.delete()
        else :
            return redirect('home')
    return redirect('user')