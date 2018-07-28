from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s %s' % (self.user.last_name, self.user.first_name, self.middle_name)

    def return_auth_person_id(self):
        return self.id

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
