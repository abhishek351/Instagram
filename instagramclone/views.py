from django.shortcuts import render,redirect,HttpResponseRedirect,reverse,get_object_or_404
from .forms import Signupform,loginform,PostForm,UserUpdateform,ProfileUpdateform,passwordChangeForm
from .models import post,profile,Comment,Notification
from django.contrib.auth import login, authenticate, update_session_auth_hash,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def home(request):
    posts=post.objects.all().order_by("-pk")
    
    context={

        'post':posts,
        
    }
       

    return render(request,"home.html",context)

def AddLike(request,pk):
    
    Post=post.objects.get(pk=pk)
        
    is_like=False

    for like in Post.likes.all():
        if like ==request.user:
            is_like=True
            break

    if not is_like:
        Post.likes.add(request.user)
        notification=Notification.objects.create(notification_type=1,from_user=request.user,to_user=Post.user,posts=Post)
    if is_like:
        Post.likes.remove(request.user)

    
    return HttpResponseRedirect(reverse('home'))




def postcreate(request):
    if  request.user.is_authenticated:
        user=request.user
        
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
                obj=form.save(commit=False)
                obj.user=user
                obj.save()
                
                return redirect(home)
        else:
            form=PostForm()
    return render(request,"postcreate.html",{'postform':form})

def login_user(request):
    if request.method == 'POST':
      form = loginform(request.POST,data=request.POST)
      if form.is_valid():
           username = form.cleaned_data['username']
           upassword = form.cleaned_data['password']
           user = authenticate(username=username, password=upassword)
           if User is not None:
               login(request, user)
               return redirect(home)

    else:
        form=loginform()

   
    return render(request,"login_user.html",{'loginform':form})



def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(home)
    else:
        form = Signupform()
    return render(request,'signup.html', {'form':form})


def postshow(request):
   
    
    return render(request,'postshow.html')


def passwordchange(request):
    if request.method =="POST":
        form=passwordChangeForm(request.user,request.POST) 

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            
            return redirect('profile')

        else:
            return redirect('passwordchange')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'passwordchange.html', {
        'form': form
    })

   
    
    return render(request,'passwordchange.html')
def edit(request):
    if request.method =="POST":
        form1=UserUpdateform(request.POST,instance=request.user)
        form2=ProfileUpdateform(request.POST,request.FILES,instance=request.user.profile)

        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect(edit)

    else:

        form1=UserUpdateform(instance=request.user)
        form2=ProfileUpdateform(instance=request.user.profile)


        
    context={
          
            'form1':form1,
            'form2':form2




        }

   
    
    return render(request,'edit.html',context)

def Profile(request,pk):
    profiles=profile.objects.get(pk=pk)
    user=profiles.user
    mypost=post.objects.filter(user=user).order_by('-datetime')
    followers=profiles.followers.all()
    numbers_of_followers=len(followers)

    if len(followers)==0:
        is_following=False

    for follower in followers:
        if follower==request.user:
            is_following=True
            break
        else: 
            is_following=False


    context={
    'user':user,
    'profiles':profiles,
    'mypost':mypost,
    'numbers_of_followers':numbers_of_followers,
    'is_following':is_following,
    }

    return render(request,'profile.html',context)

def follow(request,pk):
    profiles=profile.objects.get(pk=pk)
    profiles.followers.add(request.user)
    notification=Notification.objects.create(notification_type=3,from_user=request.user,to_user=profiles.user)

    return redirect('Profile',pk=profiles.pk)

def remove(request,pk):
    profiles=profile.objects.get(pk=pk)
    profiles.followers.remove(request.user)

    return redirect('Profile',pk=profiles.pk)




 

def logout_user(request):
    logout(request)
    return redirect(login_user)


def add_comment(request,pk):
    user = request.user
    if request.method == 'POST':
        comment= request.POST.get('comment')
        Posts = post.objects.get(id=pk)
        user_profile = User.objects.get(username=user.username)
        Comment.objects.create(
         comment=comment,
         post = Posts,
         user=user_profile   
        )
        notification=Notification.objects.create(notification_type=2,from_user=request.user,to_user=Posts.user,posts=Posts)
    return redirect('home')



def messages(request):
    return render(request,'messages.html')




        

    
    



