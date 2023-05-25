from django.urls import path
from Home import views

urlpatterns =[
    path('',views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('analysis/',views.analysis, name='analysis'),
]