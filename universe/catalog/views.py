from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Book, Author, Genre
from django.contrib.auth.decorators import login_required


@login_required()
def test(request):
    return render(request, 'catalog/test.html')


def index(request):
    """

    :param request:
    :return:
    """

    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(
        request,
        'catalog/index.html',
        context=
        {
            'num_books': num_books, 'num_authors': num_authors, 'num_visits': num_visits,
        },
    )


class BookListView(generic.ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.filter(title_icontains='war')[:5]


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


