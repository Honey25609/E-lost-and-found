from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('lost/', views.lost, name='lost'),
    path('found/', views.foundform, name='found_form'),
    # path('user/requested-items/', views.user_requested_items, name='user_requested_items'),
    path('about/', views.about, name='about'),
    path('contactUs/', views.contact, name='contact'),
    path('user_home', views.slogged_in, name='suser_home'),
    path('dashboard/', views.student_dashboard, name='dashboard'),
]