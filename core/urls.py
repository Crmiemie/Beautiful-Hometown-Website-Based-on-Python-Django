from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login'),
    path('signup/',views.signup, name='signup'),
    path('infromation/', views.information_filled, name='information'),
    path('city',views.city_show, name='city'),
    path('moment',views.moment,name='moment'),
    path('passwordchange',views.password_change,name='passwordchange'),
    path('delete/<int:pk>', views.delete_moment, name='delete'),
    path('edit/<int:pk>', views.edit_moment, name='edit')
]