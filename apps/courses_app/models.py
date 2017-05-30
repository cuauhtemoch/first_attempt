from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Description(models.Model):
    name = models.TextField(max_length=1005)
    course = models.OneToOneField(Course)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
