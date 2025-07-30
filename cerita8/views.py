import requests
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def book_list(request):
    return render(request, 'cerita8/books.html')


def get_books(request, book_name):
    url_json_books = "https://www.googleapis.com/books/v1/volumes?q="
    response = requests.get(url_json_books + book_name)
    return JsonResponse(response.json())
