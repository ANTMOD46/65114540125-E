from django.urls import path
from.views import *
urlpatterns = [

    path('A/',AS,name ='A'),
    path('E/<str:pk>',ES.as_view(),name ='E'),
]
    