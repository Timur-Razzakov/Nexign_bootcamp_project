from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from msg_sender.models import Channel, Notification_group, Notification


class Empl_requisites(models.Model):
    employee = models.ForeignKey('MyUser', verbose_name='employee', on_delete=models.CASCADE,
                                 blank=True, null=True)
    channel = models.ForeignKey(Channel, verbose_name='channel', on_delete=models.SET_NULL, blank=True,
                                null=True)
    user_details = models.CharField(max_length=255, verbose_name='user_requisites')

    def __str__(self):
        return str(self.user_details)

        # def __str__(self):
        #     return '%s, %s' % (self.last_name, self.first_name)
class Subscription(models.Model):
    employee = models.ForeignKey('MyUser', verbose_name='employee', on_delete=models.CASCADE,
                                 null=True, blank=True)
    channels = models.ManyToManyField(Channel)
    notification_group = models.ManyToManyField(Notification_group)

    def __str__(self):
        return str(self.employee)


"""Модель для итоговых данных"""


class Result(models.Model):
    employee_details = models.ManyToManyField(Empl_requisites, verbose_name="employee_requisites")
    notification = models.ForeignKey(Notification, on_delete=models.SET_NULL, verbose_name="notification",
                                     null=True, blank=True)
    # new_details = models.CharField(verbose_name='new_details', max_length=255, null=True, blank=True)

    sending_status = models.CharField(verbose_name='sending_status', max_length=90, null=True,
                                      blank=True)  # --
    process_date = models.DateTimeField(verbose_name='sent_to', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="created_at", null=True, blank=True)
    channels = models.ForeignKey(Channel, on_delete=models.SET_NULL, verbose_name='channels for send',
                                 null=True, blank=True)
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return str(self.sending_status)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Создаёт пользователя с указанным email-лом и паролем
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)  # зашифровывает пароль
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Создаёт супер пользователя для доступа к админке
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    notification_group = models.ManyToManyField(Notification_group, verbose_name='notification_group')

    receiver = models.BooleanField(default=True)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """проверяет есть ли у пользователя указанное разрешение """
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """есть  ли у пользователя разрешение на доступ к моделям в данном приложении. """
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """ Является ли пользователь администратором """
        # Simplest possible answer: All admins are staff
        return self.is_admin
