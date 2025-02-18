from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def BookListApi(request):
    books = [{
      'name': "The Alchemist",
      'author': 'Rajan Lama',
    }, {
      'name': "The Alchemist v2",
      'author': 'Ritee Lama',
    }]
    return Response(books)