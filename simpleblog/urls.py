from django.contrib.auth.views import LogoutView

from . import views
from django.urls import path

urlpatterns = [
 path('', views.general_page, name = 'just_index_page'),
 path('new_user/',views.reg_page,name = 'register_form'),
 path('add_new_user/',views.reg),
 path('to_avtorization_form/',views.avtoriz_page, name='for_avtorization'),
 path('user_avtoriz/',views.avtorization_user,name='avtorization_form'),
 path('to_profile/', views.to_profile_page, name='profile'),
 path('logout/',views.logout_view, name='out'),
 path('create_post/',views.go_to_post_form, name='post_form'),
 path('create_post/add_post/', views.add_post),
 path('sending_message/',views.to_sent_message),
 path('change_profile/',views.go_to_profile_form),
 path('save_changes_profile/',views.change_user_profile),
 path('post<slug:slug>',views.to_get_post, name='post'),
 path('comment/<int:id>/',views.to_get_comment, name='delete_comment'),
 path('profile/<int:id>/',views.to_get_current_profile, name='selected_profile'),








]

