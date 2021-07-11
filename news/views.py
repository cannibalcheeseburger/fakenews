from django.shortcuts import render,redirect
from .models import News
from django.views.generic import ListView,DetailView
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
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
    return redirect('login')

class UserListView(ListView):
    model = News
    template_name = 'userdetail.html'
    context_object_name = 'news'
    queryset = News.objects.order_by('-date')[:15]
