# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User, UserManager



class Tweet(models.Model):
    text = models.TextField(max_length=40)
    published_on = models.DateTimeField()
    user = models.ForeignKey(User)

class CustomUser(User):
    patronymic = models.CharField(max_length=100, null=True)
    City = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    objects = UserManager()

class Tutor(models.Model):
    experience = models.IntegerField()
    education = models.TextField()
    work = models.CharField(max_length=50)
    venue_of = models.CharField(max_length=50)
    avatar = models.ImageField(blank=True, upload_to="tutor_avatar", null=True)
    username = models.ForeignKey(CustomUser, primary_key=True)
    rating = models.FloatField(null=True, default=0)

class Pupil(models.Model):
    work = models.CharField(max_length=50, null=True)
    birth_date = models.DateField(null=True)
    avatar = models.ImageField(blank=True, upload_to="pupil_avatar", null=True)
    username = models.ForeignKey(CustomUser, primary_key=True)

class Additional_information(models.Model):
    tutor = models.ForeignKey(CustomUser)
    subject_name = models.CharField(max_length=50)
    section = models.CharField(max_length=100, null=True)
    additions = models.CharField(max_length=300)
    price = models.IntegerField()
    pupil_category = models.CharField(max_length=200)

class Views(models.Model):
    tutor = models.ForeignKey(to=Tutor)
    pupil = models.ForeignKey(to=Pupil)
    date = models.DateField(auto_now_add=True)

class Reviews(models.Model):
    tutor = models.ForeignKey(Tutor)
    review = models.TextField(null=True)

class Mail(models.Model):
    user = models.ForeignKey(CustomUser)
    from_email = models.EmailField()
    from_user = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

class Messages(models.Model):
    subject = models.ForeignKey(Mail)
    message = models.TextField()

class ListCity(models.Model):
    Cities = models.CharField(max_length=200)
