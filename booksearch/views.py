import pdb

from django.http import JsonResponse
from rest_framework.views import APIView
from .index_helpers import es_search


# Create your views here.

class Search(APIView):

    def get(self, request):
        query = request.query_params.get('q')
        if not query:
            return JsonResponse(
                {
                    "err": "Please provide a term to query"
                }
            )
        res = es_search(query)
        all_hits = res["hits"]["hits"]
        docs = []
        for h in all_hits:
            docs.append(
                {
                    "title": h["_source"]["title"],
                    "content": h["_source"]["content"]
                }
            )
        return JsonResponse(
            {
                "res": {
                    "took": res["took"],
                    "hits": res["hits"]["total"],
                    "all_hits": docs
                }
            }
        )
