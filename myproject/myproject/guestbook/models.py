from django.db import models
from django.utils import timezone

#create a model for comments.
#model is like a mapping between python and database.

#class name = name of table we want to create.
#inherit from models.Model
class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "<Name: {}, ID:{}>".format(self.name, self.id)