from django.shortcuts import render

# Create your views here.
from new.serializers import BooksSerializer
from new.models import Books
from rest_framework.viewsets import ModelViewSet


class BookOperations(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer