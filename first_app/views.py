from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")


def list_books(request):
    return HttpResponse("Books Page")


def book_detail(request, pk):
    return HttpResponse(f"Page of Book #{pk}")


def years(request, year):
    if year > 2025:
        raise Http404("Год должен быть меньше 2025")
    return HttpResponse(f"Year of Book #{year}")


def get_params(request):
    if request.GET:
        print(request.GET)
    return HttpResponse(
        ", ".join([f"{param} = {value}" for param, value in request.GET.items()])
    )


def redirect_view(request):
    return redirect('first_app:index', permanent=True)  # Можно указать view
    # return redirect('name', 'param')
    # return redirect(reverse('name', args=('param',))
    # HttpResponseRedirect, HttpResponsePermanentRedirect


def page_not_found(request, exception):
    return HttpResponseNotFound(f"404 Page not found: {exception}")
