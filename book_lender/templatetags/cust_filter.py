from django.utils import timezone
from django import template

register = template.Library()


@register.filter
def get_date_string(val):
    """ This is a custom filter that determines the date change was
    made to list with current time and returns appropriate message.
    """
    now_aware = timezone.now()
    timediff = now_aware - val

    if timediff.days == 0:
        return 'Today'

    elif timediff.days == 1:
        return "Yesterday"

    elif timediff.days > 1:
        return f' {timediff.days} days ago '
