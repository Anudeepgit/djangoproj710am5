from django.urls import path
from . import views
app_name='Registrationapp'
urlpatterns=[
    path('',views.input,name='input'),
    path('insert',views.insert,name='insert'),
    path('display',views.display,name='dispaly'),
]