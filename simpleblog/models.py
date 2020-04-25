from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):

    title = models.CharField('заголовок', max_length=250,null=True)
    text = models.TextField('текст',null=True)
    create_date = models.DateTimeField('дата создания',auto_now_add=True,null=True)
    to_show = models.BooleanField('отображать?', default=True,null=True)
    slug = models.SlugField('url', max_length=100, unique=True,null=True)
    user = models.ForeignKey(
        User,
        verbose_name="автор",
        on_delete=models.CASCADE,null=True)



    def __str__(self):
        return '{0}'.format(self.title)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"




class Comment(models.Model):
    text = models.TextField('текст')
    create_date = models.DateTimeField('дата создания', auto_now=True)
    to_show = models.BooleanField('отображать?', default=False)
    post = models.ForeignKey(Post,
                             verbose_name='пост',
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)
    user = models.ForeignKey(
        User,
        verbose_name="автор",
        on_delete=models.CASCADE)

    def __str__(self):
        return '{0}'.format(self.text)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"



class Profile(models.Model):

    firstname = models.CharField('имя', max_length=250, null=True)
    lastname = models.CharField('фамилия', max_length=250, null=True)
    born_data = models.CharField('день рождения', max_length=250, null=True)
    skype = models.CharField('скайп', max_length=250, null=True)
    text = models.TextField('о себе', null=True)
    fb = models.URLField('ccылка на соц сети', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return '{0}'.format(self.firstname)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профиль"


class Message(models.Model):


        message = models.TextField()
        create_date = models.DateTimeField('дата создания', auto_now=True)
        is_readed = models.BooleanField('прочитано', default=False)

        sender = models.ForeignKey(
            User, related_name='outmassages',
            verbose_name='отправитель',
            on_delete=models.CASCADE,null=True)

        reciver = models.ForeignKey(
            User,related_name='inmassages',
            verbose_name='получатель',
            on_delete=models.CASCADE, null=True)

        def __str__(self):
            return '{0}'.format(self.message)

        class Meta:
            verbose_name = "Cообщение"
            verbose_name_plural = "Сообщения"


