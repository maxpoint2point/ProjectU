# from django.contrib import admin
from django.urls import path
from UTMWatch.views import *

app_name = 'UTMWatch'
urlpatterns = [
    path('workplace/create/', WorkPlaceCreateView.as_view()),
    path('workplace/all/', WorkPlaceListView.as_view()),
    path('workplace/<int:pk>/', WorkPlaceDetailView.as_view()),
    path('ou/create/', OUCreateView.as_view()),
    path('ou/all/', OUListView.as_view()),
    path('ou/<int:pk>/', OUDetailView.as_view()),
]
