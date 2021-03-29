from django.utils import timezone


def uemail_auth_num_time_check(updated_at):
    now = timezone.now()
    interval = now - updated_at
    s = interval.total_seconds()
    # limit 5 minutes (300s)
    if s > 300:
        return False
    else:
        return True