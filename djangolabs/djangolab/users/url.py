# from django.urls import path
# from .views import *
# from django.contrib.auth.views import LoginView,LogoutView
# urlpatterns=[
   
#     path('',LoginView.as_view(
#         template_name='users/login.html'
#     ),name='login'),
    
#     path('Logout/',LogoutView.as_view(next_page='/login'),name='logout'),
   
#     # path('Reg/',rege.as_view(),name='Reg'),
    
# ]

from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
    # path('Loginnative/',Signin.as_view(),name='Loginnative'),
    path('',LoginView.as_view(
        template_name='users/login.html'
    ),name='Login'),
    # path('Logoutnative/',SignOutView.as_view(),name='Logoutnative'),
    path('Logout/',LogoutView.as_view(next_page='/Login'),name='Logout'),
    # path('Reg/',Regview,name='Reg'),
    path('Reg/',SignupView.as_view(),name='Reg'),
    # path('Regnariv/',Signup.as_view(),name='Regnative'),
]