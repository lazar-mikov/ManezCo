from django.urls import path, include
from .import  views

urlpatterns=[
     path('', views.index, name='index'),
     path('register/',views.register, name='register'),
     path('adult_register/',views.adult_register.as_view(), name='adult_register'),
     path('child_register/',views.child_register.as_view(), name='child_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     path('books/', include('books.urls')),
]