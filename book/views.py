from django.shortcuts import render
from .models import Books
from .serializers import BookSerializer
from rest_framework import generics

class BookList(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
class BookDetail(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
class BookCreate(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
class Bookcreate(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
class BookUpdeteDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class =BookSerializer
