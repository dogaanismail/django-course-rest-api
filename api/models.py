from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=False)
