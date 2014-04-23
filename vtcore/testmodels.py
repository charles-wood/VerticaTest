from django.db import models as djangomodels
from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField


class Post(djangomodels.Model):
	title = djangomodels.CharField()
	text = djangomodels.TextField()
	tags = ListField()
	comments = ListField()
	new_thing = djangomodels.IntegerField(null=True)

	def __unicode__(self):
		return self.title
