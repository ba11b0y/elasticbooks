from elasticsearch_dsl import Index, Document, Text, analyzer, tokenizer

books = Index('books')

my_analyzer = analyzer('my_analyzer',
                       tokenizer=tokenizer('trigram', 'edge_ngram', min_gram=1, max_gram=20),
                       filter=['lowercase']
                       )


@books.document
class Book(Document):
    title = Text(analyzer=my_analyzer)
    content = Text(analyzer=my_analyzer)
