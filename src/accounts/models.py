from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

def upload_path(instance, filename):
    return '/'.join(['profile_pics', str(instance.email), filename])

class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=80)
    email = models.EmailField(_('email address'), unique=True)
    image = models.ImageField(default='default.jpg', upload_to=upload_path)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return "{}".format(self.email)