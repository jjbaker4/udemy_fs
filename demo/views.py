from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    #comma is here because we want python to treat this as a tuple


#class Another(View):
#
#    def get(self, request):
#        return HttpResponse('This is another function inside a class')


#class BookCount(View):
#
#    books = Book.objects.all()
#
#    output = f"We have {len(books)} books in DB"
#
#    def get(self, request):
#        return HttpResponse(self.output)


class BookList(View):

    books = Book.objects.all()
    output = 'All Books:<br>'

    for book in books:
        output += f"We have {book.title} book with ID {book.id}<br>"

    def get(self, request):
        return HttpResponse(self.output)


class BookListPublished(View):

    books = Book.objects.filter(is_published=True)
    output = 'All Published Books:<br>'

    for book in books:
        output += f"We have {book.title} book with ID {book.id}<br>"

    def get(self, request):
        return HttpResponse(self.output)


class Book2(View):

    book = Book.objects.get(id=2)
    output = f"We have {book.title} book with ID {book.id}<br>"

    def get(self, request):
        return HttpResponse(self.output)


def first(request):
    return HttpResponse('First message from views')


def first_template(request):
    return render(request, 'first_temp.html')


def dynamic_template(request):
    books = Book.objects.all()
    return render(request, 'dynamic_temp.html', {'books': books})