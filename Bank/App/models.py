from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver

# Create your models here.

class TrustCall(models.Model):
    # name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    customers = models.IntegerField(default=528, null=True)
    employees = models.IntegerField(default=1530, null=True)
    deposit = models.IntegerField(default=50, null=True)

    # def __str__(self):
    #     return self.name.username

class Users(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_of_birth = models.DateTimeField(null=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    phone_number = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)
    status = models.CharField(max_length=20, null=True)
    address = models.TextField(null=False)
    account_number = models.IntegerField(null=True, default=110)
    balance = models.IntegerField(default=0, null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name.username

@ receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        Users.objects.create(name=instance)


class Message(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    email = models.EmailField()
    sent_time = models.DateTimeField(verbose_name="last login", auto_now=True)

    def __str__(self):
        return self.email

def save_user_message(sender, instance, created, **kwargs):
    if created:
        Message.objects.create(name=instance)

class Contact(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    email = models.EmailField()
    sent_time = models.DateTimeField(verbose_name="last login", auto_now=True)
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.email

def save_user_contact(sender, instance, created, **kwargs):
    if created:
        Contact.objects.create(name=instance)

class Loan(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(null=False, max_length=None)
    message = models.TextField()
    to = models.CharField(max_length=50, null=False)
    sent_time = models.DateTimeField(verbose_name="last login", auto_now=True)

    def __str__(self):
        return self.amount

def save_user_loan(sender, instance, created, **kwargs):
    if created:
        Loan.objects.create(name=instance)

class Payment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(null=False, max_length=None)
    message = models.TextField()
    type = models.TextField()
    to = models.CharField(max_length=50, null=False)
    sent_time = models.DateTimeField(verbose_name="last login", auto_now=True)

    def __str__(self):
        return self.amount

def save_user_payment(sender, instance, created, **kwargs):
    if created:
        Payment.objects.create(name=instance)

class Staff(models.Model):
    image = models.ImageField(null=False)
    position = models.TextField()
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

def save_user_staff(sender, instance, created, **kwargs):
    if created:
        Staff.objects.create(name=instance)
