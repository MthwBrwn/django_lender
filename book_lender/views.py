from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import login_required


@login_required
def book_list_view(request):
    """ This handles the request/response to the the Database and collects all the objects
    """
    context = {
        'books': get_list_or_404(Book)
    }
    return render(request, 'books/book_list.html', context)


@login_required
def book_detail_view(request, pk=None):
    """ This handles the request/response to the the Database and collects one specified object
    """
    context = {
        'book': get_object_or_404(Book, id=pk)
    }
    return render(request, 'books/book_detail.html', context)





