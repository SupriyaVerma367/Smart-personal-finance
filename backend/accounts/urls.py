from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('test/',views.test_api,name='test_api'),
    path('register/',views.register_user,name='register'),
    path('login/',obtain_auth_token,name='login'),
]