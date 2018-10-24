from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from booksearch.index_documents import Book, books
from elasticsearch.exceptions import NotFoundError


class BookModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


@receiver(post_save, sender=BookModel)
def index(instance, **kwargs):
    """Signal to index in Elasticsearch"""
    # Checks for a mapping, if not found creates one
    try:
        books.get_mapping()
    except NotFoundError:
        Book.init()
    book = Book(title=instance.title, content=instance.content)
    book.meta.id = instance.pk
    book.save()
    print("Indexed in ElasticSearch!!")
    return None
