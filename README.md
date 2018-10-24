#### A simple project to get familiar with `elasticsearch_dsl`

#### Setup Instructions 

 - Clone the project
 - Install requirements with `pip install -r requirements.txt`
 - Setup Elasticsearch

#### Usage
 ##### Indexing
 - Run management command with `python manage.py index "path/to/file"`
 - Input the book title
 ##### Searching
 - Provide query as a param to `localhost:8000/booksearch`
 - Example query - `localhost:8000/booksearch?q=sample`