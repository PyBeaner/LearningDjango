__author__ = 'PyBeaner'

# Creating objects
"""
>>> from blog.models import Blog
>>> b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
>>> b.save()
"""

# Updating
"""
>>> b.name = "New Name"
>>> b.save()
"""

# Updating ForeignKey
"""
entry = Entry.objects.get(pk=1)
cheese_blog = Blog.objects.get(name="Cheddar Talk")
entry.blog = cheese_blog
entry.save()
"""

# Updating ManyToManyKey
"""
joe = Author.models.create(name="job")
entry.authors.add(joe)

# add mutliple records
>>> john = Author.objects.create(name="John")
>>> paul = Author.objects.create(name="Paul")
>>> george = Author.objects.create(name="George")
>>> ringo = Author.objects.create(name="Ringo")
entry.authors.add(john,paul,george,ringo)
"""