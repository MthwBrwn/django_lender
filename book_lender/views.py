from django.shortcuts import render
from .models import Note


def book_list_view(request):
    """
    """
    context = {}
    return render(request, 'books/book_list.html', context)


def book_detail_view(request):
    """
    """
    context = {}
    return render(request, 'books/book_detail.html', context)





