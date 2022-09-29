from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from.forms import  registrationform, updateuserform, profileupdate
from django.contrib.auth.decorators import login_required
from.forms import addpostform
from .models import post
from django.views.generic import DetailView,UpdateView
# Create your views here.

def index (request):
    posts=post.objects.all(). order_by('-id')
    
    return render (request, 'index.html', {'posts':posts})
@login_required
def addpost(request):
    if request.method=='POST':
        form=addpostform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
            
            

    else:
        form=addpostform()

    return render (request, 'addpost.html', {'form':form})



def register(request):
    if request.method =='POST':
        form=registrationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            

    else:
        form=registrationform(request.POST)
    return render (request, 'register.html', {'form':form})
#i have to input the else statement for avoid '' refrence before assignment 


#def login (request):
    #return render (request,('login.html')) and it dosent need views for it too 
    
@login_required
def updateuser(request):
    if request.method =='POST':
        u_form=updateuserform(request.POST, instance=request.user)
        p_form=profileupdate(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            return redirect('author')
    else:
         u_form=updateuserform(instance=request.user)
         p_form=profileupdate(instance=request.user.profile)
       
    return render(request, 'updateuser.html', {'p_form':p_form, 'u_form':u_form})


@login_required
def author(request):
    return render (request, 'author.html')

@login_required
def editpost(request, post_id):
    form=post.objects.get(pk=post_id)
    return render (request, 'editpost.html', {'form':form})
'''
def article(request, id):
    post.objects.get(id=id)
    return render(request, 'article.html')
'''
class articledetailview (DetailView):
    model=post
    template_name='article.html'

class editview(UpdateView):
    model=post
    template_name='editpost.html'
    fields=['title', 'title_tags', 'body'] 


    