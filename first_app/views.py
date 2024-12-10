from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

from first_app.models import Category, Product


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


def template(request):
    context = {
        'users': [
            {'name': 'Max', 'age': 30, 'phone': '79998887766'},
            {'name': 'Alex', 'age': 25, 'phone': '78887776655'},
            {'name': 'Denis', 'age': 35, 'phone': '71234567890'},
        ]
    }
    return render(request, 'first_app/template.html', context)


def custom_tags(request):
    return render(request, 'first_app/custom_tags.html')


def categories_list(request):
    context = {'categories': Category.objects.all()}
    return render(request, 'first_app/categories.html', context)


def category_detail(request, category_slug):
    context = {
        'category': get_object_or_404(Category, slug=category_slug),
        'products': Category.objects.get(slug=category_slug).product_set.all(),
    }
    return render(request, 'first_app/category.html', context)


def product_detail(request, product_slug):
    prod = get_object_or_404(Product, slug=product_slug)
    return render(request, 'first_app/product_detail.html', {'product': prod},)
