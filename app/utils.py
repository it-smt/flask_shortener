import random
import string

from app.models import URLmodel


def get_short():
    while True:
        short = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        if URLmodel.query.filter(URLmodel.short == short).first():
            continue
        return short