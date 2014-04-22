from django.db import models

from djangotoolbox.fields import ListField


class Post(models.Model):
	title = models.Charfield()
	text = models.TextField()
	tags = ListField()
	comments = ListField()