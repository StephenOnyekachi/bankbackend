from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('user_login/', views.user_login, name='user_login'),
    path('signup_login/', views.signup_login, name='signup_login'),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('signup2/', views.signup2, name='signup2'),
    path('user_logout/', views.user_logout, name='user_logout'),


    path('all/', views.all, name='all'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('change/', views.change, name='change'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('loan/', views.loan, name='loan'),
    path('message/', views.message, name='message'),
    path('profile/', views.profile, name='profile'),

    path('trying/', views.trying, name='trying'),


    path('edit/<int:pk>/', views.edit, name='edit'),
    path('edit_trustcall/<int:pk>/', views.edit_trustcall, name='edit_trustcall'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('delete_message/<int:pk>/', views.delete_message, name='delete_message'),

    path('about/', views.index, name='about'),
    path('about/', views.index, name='about'),
    path('about/', views.index, name='about'),
]

