# django
# from django.db import models
# standard library
from uuid import uuid4

# django
from django.utils import timezone


# Create your models here.
def file_path(instance, name):
    """
    Generic method to give to a FileField or ImageField in it's upload_to
    parameter.

    This returns the name of the class, concatenated with the id of the
    object and the name of the file.
    """
    date = timezone.datetime.now().date()
    return f"{instance.__class__.__name__}/{date}/{uuid4()}/{name}"
