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

# Retrieving objects
"""
>>> all_entries = Entry.objects.all()
# filters
>>> Entry.objects.filter(pub_date__year=2006)
# chaining filters
>>> Entry.objects.filter(
        pub_date__year=2006
    ).exclude(
        pub_date__gte=datetime.now()
    )
# QuerySets are lazy
>>> q = Entry.objects.filter(headline__startswith="What")
>>> q = q.filter(pub_date__lte=datetime.date.today())
>>> q = q.exclude(body_text__icontains="food")
# in fact it hits the database only once
>>> print(q)
"""

# Limiting QuerySets
"""
# just like the list-slicing(But -1 is not a valid index)
>>> Entry.objects.all()[5:10:2]
"""

# Fields Lookups
"""
# double-underscore
# field__lookuptype=value
# foreign-key lookup:
>>> Entry.objects.filter(blog_id=3)
# exact match
>>> Entry.objects.filter(headline__exact="Hello") # Explicit
>>> Entry.objects.filter(headline="Hello") # implicit
# case-insensitive match
>>> Entry.objects.filter(headline_iexact="hello") # would match "Hello","hello",""HELLO"..
# (i)contains(sql like), (i)startswith, (i)endswith
Entry.objects.get(headline__contains='Lennon')
"""

# Fields on the same model
# F expressions
"""
from django.db.models import F
Entry.objects.filter(n_comments__gt=F('n_pingbacks'))
"""

# pk(Primary Key) shortcut
pass

# Caching and QuerySets
"""
# executed twice
>>> print([e.headline for e in Entry.objects.all()])
>>> print([e.pub_date for e in Entry.objects.all()])
# save the queryset to reuse
>>> queryset = Entry.objects.all()
>>> print([p.headline for p in queryset]) # Evaluate the query set.
>>> print([p.pub_date for p in queryset]) # Re-use the cache from the evaluation.
# not cached
>>> queryset = Entry.objects.all()
>>> print(queryset[5]) # queries the db
>>> print(queryset[5]) # queries the db again
# if the entire queryset has already been evaluated, the cache will be checked instead:
# operations like "bool","list","in" would populate the cache
"""

# Complex lookups with Q(Q expressions)
"""
from django.models.db import Q
Poll.objects.get(
    Q(question__startswith='Who'),
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
)
"""

# Comparing
"""
a_entry == b_entry
# Comparisons will always use the primary key(ID,or whatever)
a_entry.id == b_entry.id
"""

# Deleting objects
"""
b = Blog.objects.get(pk=1)
# the entries of this blog would also be deleted!
# ON DELETE CASCADE(default),you can change it in on_delete argument of the ForeignKey
b.delete()

# deleting called on the object-manager is not available to prevent deleting all the entries
-->Blog.objects.delete()
instead: use Blog.objects.all().delete()
"""


# Copying objects
"""
entry.id = None
entry.save()
"""

# Updating multiple objects
"""
Entry.objects.filter(id__gte=4).update(headline="Something else")
Entry.objects.filter(id__gt=10).update(blog=b) # update on the ForeignKey
"""

"""
Note:
    It doesn��t run any save() methods on your models, or emit the pre_save or post_save signals (which are a consequence of calling save()), or honor the auto_now field option
# loop over to save

for item in queryset:
    item.save()
"""
