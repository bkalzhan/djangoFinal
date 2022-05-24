from django.contrib import admin
from django.urls import path, include
from .views import BooksViewSet, JournalsViewSet


urlpatterns = [
    path('books/', BooksViewSet.as_view({'get': 'list',
                                         'post': 'create'})),
    path('books/<int:pk>/', BooksViewSet.as_view({'get': 'retrieve',
                                                  'delete': 'destroy',
                                                  'put': 'update'})),
    path('journals/', JournalsViewSet.as_view({'get': 'list',
                                         'post': 'create'})),
    path('journals/<int:pk>/', JournalsViewSet.as_view({'get': 'retrieve',
                                                  'delete': 'destroy',
                                                  'put': 'update'})),
]