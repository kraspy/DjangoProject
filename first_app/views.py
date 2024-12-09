from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Hello, world!')


def list_books(request):
    return HttpResponse('Books Page')


def book_detail(request, pk):
    return HttpResponse(f'Page of Book #{pk}')


def years(request, year):
    return HttpResponse(f'Year of Book #{year}')
