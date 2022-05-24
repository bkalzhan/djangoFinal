from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Book, Journal
from .serializers import BookSerializer, JournalSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve', 'create', 'update', 'destroy']:
            return BookSerializer


class JournalsViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve', 'create', 'update', 'destroy']:
            return JournalSerializer
