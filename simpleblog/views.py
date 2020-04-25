from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import View
# Create your views here.
from django.contrib.auth import logout

from .models import *
from .forms import ProfileForm, PostForm, MessageForm, CommentForm


def general_page(request):
    """ функция ведет на главную страницу"""

    template = 'simpleblog/index.html'

    users = User.objects.filter(post__isnull=False)
    print('general_page:',users)

    return render(request, template,{'users': users})


def reg_page(request):
    """ функция ведет на страницу c формой регистрации"""
    template = 'simpleblog/registration.html'
    return render(request, template)


def avtoriz_page(request):
    template = 'simpleblog/avtorization.html'
    return render(request, template)


def reg(request):
    """ функция обрабатывает форму регистрации"""

    username = request.POST['login']

    password = request.POST['password']
    password2 = request.POST['password2']
    email = request.POST['email']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']

    newuser = User.objects.create_user(
        username=username, password=password, email=email, first_name=firstname, last_name=lastname)

    new_profile = Profile()

    new_profile.user = newuser

    new_profile.save()


    print('for_avtorization')

    return redirect('for_avtorization')


def avtorization_user(request):
    """ функция обрабатывает форму регистрации"""
    username = request.POST['login']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('just_index_page')
        else:
            return redirect('register_form')


def logout_view(request):
    logout(request)
    return redirect('just_index_page')



def go_to_profile_form(request):
    """ функция ведет на страницу c формой для редактирования профиля"""
    user = request.user
    user_profile_form = ProfileForm(user)
    template = 'simpleblog/profile_form.html'

    print('go_to_profile_form:')

    return render(request, template, {'user_profile': user_profile_form})



def go_to_post_form(request):
    """ функция ведет на страничку с формой добавления поста"""

    form_post = PostForm(user=request.user)
    template = 'simpleblog/post_form.html'

    return render(request, template, {'form_post': form_post})

def go_to_post_detail(request):

    template = 'simpleblog/post_detail.html'

    return render(request,template)


def add_post(request):
    """ функция ведет на бработку формы поста"""

    form_post = PostForm(request.POST, user=request.user)

    if form_post.is_valid():
        form_post.save()

        return redirect('just_index_page')
    else:
        print('bad form')
        return redirect('post_form')



def to_get_post(request, **kwargs):

    template = 'simpleblog/post_detail.html'
    post = get_object_or_404(Post, slug=kwargs.get("slug"))

    comments = Comment.objects.filter(post=post)


    form_comment = CommentForm()

    return render(request,template,{'post':post, 'form_comment':form_comment,'comments':comments})



def to_get_comment(request, id):

    selected_comment = get_object_or_404(Comment, id=id)
    selected_comment.delete()
    return redirect('post_detail')



def to_get_current_profile(request, id):
    """функция ведет на другие профиля, которые может просматривать авторизированный юзер"""
    user = request.user

    current_user = User.objects.get(id=id)
    user_prof = current_user.profile

    print('Method to_get_current_profile', 'reciver:', current_user,'sender:',request.user)
    template = 'simpleblog/another_profile.html'

    message_form = MessageForm(user,current_user)

    return render(request, template, { 'user_prof': user_prof, 'message_form': message_form })



def to_sent_message(request):
    """ функция ведет на бработку формы c лс"""
    user = User.objects.get(id= request.POST['sender'])
    current_user = User.objects.get(id= request.POST['reciver'])


    message_form = MessageForm(request.POST,current_user)


    if message_form.is_valid():
        message_form.save()
        return redirect('just_index_page')
    else:
        print('som   ething went wrong')
        return redirect('just_index_page')



def to_profile_page(request):
    """функция позволяет просматривать собственный профиль юзера"""

    current_user = request.user
    user_prof = current_user.profile

    print('Method to_profile_page', 'user_prof', user_prof, 'user:', current_user)

    template = 'simpleblog/profile.html'

    return render(request, template, {'user_prof': user_prof})

def change_user_profile(request):
    """ функция ведет на бработку формы c профилем"""

    user = request.user
    # The get_object method returns queryset i.e list of records, instead of instance.To get instance you can use first() on filter() . This will gives you first occurrence.
    user_prof = Profile.objects.all().filter(user=request.user).first()

    user_profile_form = ProfileForm(user, request.POST, instance=user_prof)
    if user_profile_form.is_valid():

         user_profile_form.save()

         return redirect('profile')
    else:
        print('bad form')
        return redirect('just_index_page')

















