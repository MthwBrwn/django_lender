from django.test import TestCase, RequestFactory
from .models import Book
from django.contrib.auth.models import User


class TestBookModel(TestCase):
    """
    """
    def setUp(self):
        """ This is he set up for each one of the tests
        """
        Book.objects.create(title='TestBook1', author='testAuthor1', year='1999')
        Book.objects.create(title='TestBook2', author='testAuthor2', year='1998')
        Book.objects.create(title='TestBook3', author='testAuthor3', year='1997')

    def test_book_titles(self):
        """This test checks to make sure the model properly stores the title in the DB
        """
        one = Book.objects.get(title="TestBook3")
        self.assertEqual(one.title, "TestBook3")

    def test_book_authors(self):
        """This test checks that the author is properly stored
        """
        authors = Book.objects.all()
        self.assertEqual(authors[2].author, "testAuthor3")

    def test_book_year(self):
        """ This test checks that the year is correct
        """
        one = Book.objects.get(title='TestBook1')
        self.assertEqual(one.year, "1999")

    def test_book_default_status(self):
        """ This checks that the status is defaulted to checked in
        """
        one = Book.objects.get(title='TestBook1')
        self.assertEqual(one.status, "checked_in")


class TestBooksViews(TestCase):
    """ this establishes a class in which to test context in the views
    """
    def setUp(self):
        self.request = RequestFactory()

        self.book = Book.objects.create(title='TestBook1', author='testAuthor1', year='1999')
        Book.objects.create(title='TestBook2', author='testAuthor2', year='1998')
        Book.objects.create(title='TestBook3', author='testAuthor3', year='1997')

    def test_book_list_view_context(self):
        """
        """
        from .views import book_list_view
        request = self.request.get('')
        response = book_list_view(request)
        self.assertIn(b'TestBook1', response.content)

    def test_book_list_view_status(self):
        """
        """
        from .views import book_list_view
        request = self.request.get('')
        response = book_list_view(request)
        self.assertEqual(200, response.status_code)

    def test_book_detail_view_context(self):
        """
        """
        from .views import book_detail_view
        request = self.request.get('')
        response = book_detail_view(request, self.book.id)
        self.assertIn(b'TestBook1', response.content)

    def test_book_detail_view_failure(self):
        """
        """
        from .views import book_detail_view
        from django.http import Http404
        request = self.request.get('')
        with self.assertRaises(Http404):
            book_detail_view(request, '0')
