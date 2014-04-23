import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vt.settings")

from vtcore import testmodels

# post = testmodels.Post.objects.create(title='Word up yo 222222!', text='Pow muthafucka 2222!', tags=['mongo2', 'slj2'])

# # post.comments.extend(['woo woo', 'derp'])

# post.save()

# print post
# # print post.comments

for p in testmodels.Post.objects.all():
	try:
		print p.new_thing
	except:
		print "no"
