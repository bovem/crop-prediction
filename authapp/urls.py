from django.urls import path
from .views import signin, signup, signout, prediction
from . import views

urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='signout'),
    path('result', prediction, name='result'),
    
]