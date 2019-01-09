from django.test import TestCase
from .models import Book


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
        self.assertEqual(authors[2], "testAuthor3")

    def test_book_year(self):
        """ This test checks that the year is correct
        """
        one = Book.object.get(title='TestBook1')
        self.assertEqual(one.year, "1999")

    def test_book_default_status(self):
        """ This checks that the status is defaulted to checked in
        """
        one = Book.object.get(title='TestBook1')
        self.assertEqual(one.status, "checked_in")


