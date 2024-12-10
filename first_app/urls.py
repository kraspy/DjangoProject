from django.conf.urls import handler404
from django.urls import path, register_converter
from first_app import views, converters

register_converter(converters.FourDigitYearConverter, 'year4')

app_name = 'first_app'

urlpatterns = [
    path(
        '',
        views.index,
        name='index',
    ),
    path(
        'books/',
        views.list_books,
        name='list_books',
    ),
    path(
        'books/<int:pk>/',
        views.book_detail,
        name='book_detail',
    ),
    path(
        'years/<year4:year>/',
        views.years,
        name='years',
    ),
    path(
        'get_params/',
        views.get_params,
        name='get_params',
    ),
    path(
        'redirect',
        views.redirect_view,
        name='redirect',
    ),
    path(
        'template',
        views.template,
        name='template',
    ),
]
