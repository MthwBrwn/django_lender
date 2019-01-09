from django.db import models

class Book(models.Model):
    """
    """
    cover_image   #: An image field
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    year = models.CharField(max_length=4)
    STATES = [
        ('checked-in', 'Checked-In')
        ('checked-out', 'Checked-Out')
    ]
    status = models.CharField(max_length=48, default='checked-in', choices=STATES)
    date_added  #: Auto-generated date field
    last_borrowed  #: Auto-updated date field

    def __repr__(self):
        """
        """
        pass

    def __str__(self):
        """
        """
        pass
