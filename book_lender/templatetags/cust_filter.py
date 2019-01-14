from dhango.utils import timezone


def get_date_string(val):
    """
    """
    now_aware = timezone.now()
    timediff = val - now_aware

    if timediff.days == 0:
        return 'Today'

    elif timediff.days == 1:
        return "Tomorrow"

    elif timediff.days > 1:
        return f'In {timediff.days} days'
