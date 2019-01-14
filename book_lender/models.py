from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User


class Book(models.Model):
    """ This is the class Book which is the model for our book object
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    cover_image = models.ImageField(upload_to='media', default='img.png')
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)

    YEARS = [(str(i), str(i)) for i in range(1454, 2019)]
    year = models.CharField(max_length=5, choices=YEARS)

    STATES = [
        ('checked_in', 'Checked In'),
        ('checked_out', 'Checked Out'),
    ]
    status = models.CharField(max_length=48, default='checked_in', choices=STATES)
    date_added = models.DateTimeField(default=timezone.now)
    last_borrowed = models.DateTimeField(auto_now=True)

    def __repr__(self):
        """ Repr returns the title and then the date added and last borrowed date
        """
        return f'{self.title}, {self.author}, {self.year}, {self.status},'

    def __str__(self):
        """ str gives back basic information about the class objects
        """
        return f'{self.title}, {self.author}, {self.year}, {self.status} '


@receiver(models.signals.post_save, sender=Book)
def set_note_completed_date(sender, instance, **kwargs):
    """
    """
    if instance.status == 'Checked Out' and not instance.last_borrowed:
        instance.last_borrowed = timezone.now
        instance.save()
