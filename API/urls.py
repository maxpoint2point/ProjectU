# from django.contrib import admin
from django.urls import path
from API.views import *

app_name = 'API'
urlpatterns = [
    path('workplace/create/', WorkPlaceCreateView.as_view()),
    path('workplace/all/', WorkPlaceListView.as_view()),
    path('workplace/<int:pk>/', WorkPlaceDetailView.as_view()),

    path('ou/create/', OUCreateView.as_view()),
    path('ou/all/', OUListView.as_view()),
    path('ou/<int:pk>/', OUDetailView.as_view()),

    path('rest/all', RestListView.as_view()),
    path('rest/<int:pk>/', RestDetailView.as_view()),
    path('rest/create/', RestCreateView.as_view()),
    path('workplace/<int:pk>/exchange', Exchange.as_view()),
]
