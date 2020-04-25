from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField, SelectDateWidget
from django.http import request, QueryDict

from .models import Profile, Post, Message, Comment


class ProfileForm(ModelForm):


    class Meta:
        model = Profile
        fields = ('firstname', 'lastname','born_data','skype','text','fb','user')

    def __init__(self, user,*args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        #queryset = Profile.objects.filter(user=user)

        self.fields['firstname'].initial = user.profile.firstname
        self.fields['lastname'].initial = user.profile.lastname
        self.fields['born_data'].initial = user.profile.born_data
        self.fields['skype'].initial = user.profile.skype
        self.fields['text'].initial = user.profile.text
        self.fields['fb'].initial = user.profile.fb
        self.initial['user'] = user



class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('user','title','text','slug')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PostForm, self).__init__(*args, **kwargs)
        self.initial['user'] = self.user

    def save(self, commit=True):
        '''логический boolean commit параметр, который позволяет указать, должен ли объект сохраняться в базе данных.
           Если commit имеет значение False, метод save() вернет экземпляр модели, но не сохранит его в базе данных.'''
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance



class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = ('message','sender','reciver',)

    def __init__(self, user, current_user, *args, **kwargs):

        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['sender'].initial = user
        self.fields['reciver'].initial = current_user
        print('MessageForm:','user:',user,'current:',current_user)





class CommentForm(ModelForm):

    class Meta:
        model = Comment

        fields = ('user', 'text',)

