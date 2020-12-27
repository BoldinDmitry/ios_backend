import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.db import models

from universities.models import EdProgram
from users.managers import UserManager


class EgeResults(models.Model):
    total = models.IntegerField(default=0)
    russian = models.IntegerField(default=0)
    mathProf = models.IntegerField(default=0)
    mathBase = models.IntegerField(default=0)
    biology = models.IntegerField(default=0)
    informatics = models.IntegerField(default=0)
    socialStudies = models.IntegerField(default=0)
    physics = models.IntegerField(default=0)
    chemistry = models.IntegerField(default=0)
    history = models.IntegerField(default=0)
    geography = models.IntegerField(default=0)
    english = models.IntegerField(default=0)
    german = models.IntegerField(default=0)
    french = models.IntegerField(default=0)
    chinese = models.IntegerField(default=0)
    spanish = models.IntegerField(default=0)
    literature = models.IntegerField(default=0)


class Achievements(models.Model):
    goldenMedal = models.BooleanField(default=False)
    gto = models.BooleanField(default=False)
    volunteering = models.BooleanField(default=False)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), blank=True, null=True, unique=True)
    password = models.CharField(_('password'), max_length=128, default=uuid.uuid4)
    token = models.TextField(_('token'), default=uuid.uuid4, unique=True)
    first_name = models.CharField(_('first name'), max_length=70)
    last_name = models.CharField(_('last name'), max_length=70)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    ege_results = models.ForeignKey(EgeResults, on_delete=models.CASCADE, blank=True, null=True)
    achievements = models.ForeignKey(Achievements, on_delete=models.CASCADE, blank=True, null=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.token


class Feedback(models.Model):
    title = models.TextField()
    message = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    email = models.EmailField()


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    education_program = models.ForeignKey(EdProgram, on_delete=models.CASCADE)
