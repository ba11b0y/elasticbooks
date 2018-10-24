from .index_documents import Book
from elasticsearch_dsl import Q
from elasticsearch_dsl import connections

connections.create_connection(hosts=['localhost'], timeout=20)


def es_search(query):
    """Search function which matches both in the book title and content"""
    s = Book.search()
    fquery = Q("match", title=query)
    squery = Q("match", content=query)
    cquery = fquery | squery
    search_query = s.query('bool', filter=[cquery])
    res = search_query.execute()
    return res.to_dict()
