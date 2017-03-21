from django.db import models

# Create your models here.
class Patron(models.Model):
    first_name = models.CharField(max_length=264, blank=True)
    last_name = models.CharField(max_length=264, blank=True)
    library_card_number = models.CharField(max_length=13, blank=True)
    phone_number = models.CharField(max_length=24, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class GoogleAccount(models.Model):
    patron = models.OneToOneField(
        Patron,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    username = models.CharField(max_length=264, blank=True)
    password = models.CharField(max_length=264, blank=True)


class YahooAccount(models.Model):
    patron = models.OneToOneField(
        Patron,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    username = models.CharField(max_length=264, blank=True)
    password = models.CharField(max_length=264, blank=True)


class HotmailAccount(models.Model):
    patron = models.OneToOneField(
        Patron,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    username = models.CharField(max_length=264, blank=True)
    password = models.CharField(max_length=264, blank=True)


class OtherAccount(models.Model):
    patron = models.OneToOneField(
        Patron,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    service = models.CharField(max_length=264, blank=True)
    username = models.CharField(max_length=264, blank=True)
    password = models.CharField(max_length=264, blank=True)
