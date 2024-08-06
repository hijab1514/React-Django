from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .models import Book


def index(request):
    # View function to handle requests to the homepage
    return HttpResponse("Hello, world!")


class MyView(View):
    def get(self, request):
        # Logic to handle a GET request
        return HttpResponse("Hello, this is a GET response!")

        class MyView(View):
    def post(self, request):
        # Logic to handle a POST request
        return HttpResponse("Hello, this is a POST response!")

# views.py


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
