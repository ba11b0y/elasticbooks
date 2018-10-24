import pdb

from django.core.management.base import BaseCommand
import textract
from textract.exceptions import MissingFileError
from booksearch.models import BookModel
from elasticsearch_dsl import connections

connections.create_connection(hosts=['localhost'], timeout=20)


class Command(BaseCommand):
    """Management Command to index a document in ElasticSearch"""
    # TODO: Support Bulk Indexing
    help = 'Index the book in ElasticSearch'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        file_path = options["path"][0]
        try:
            text = str(textract.process(file_path))
            title = input("Please enter the title of the book ")
            book = BookModel(title=title, content=text)
            book.save()
        except MissingFileError:
            print("File not found, please mention the exact file path.")
        return None
