from django.shortcuts import render


def home_view(request):
    """ This method renders the home view
    """
    return render(request, 'generic/home.html', {'message': ''})
