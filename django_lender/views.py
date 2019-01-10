from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    """ This method renders the home view. It is protected with a log in required decorator
    """
    return render(request, 'generic/home.html', {'message': ''})
