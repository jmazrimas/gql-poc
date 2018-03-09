from django.http import HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import json
from graphene import Schema

from graph_ql.schema import Query

def index(request):
    """
    :param request:
    :return: a list of all factories, no filtering (yet)
    """

    cursor = connection.cursor()
    query = "select id, name, created_at from factory order by id"
    cursor.execute(query, (),)

    results = cursor.fetchall()
    factory_obj = []
    for factory in results:
        factory_obj.append({
            'id': factory[0],
            'name': factory[1],
            'created_at': str(factory[2])
        })

    response = HttpResponse(json.dumps(factory_obj))
    response.status_code = 200
    response['Access-Control-Allow-Origin'] = '*'
    return response

@csrf_exempt
def gql(request):
    """
    :param request:
    :return: a list of all factories, no filtering (yet)
    """

    req_body = request.body.decode('utf-8')
    schema = Schema(query=Query)

    result = schema.execute(req_body)

    if result.errors:
        print('ERROR:', result.errors)

    response = HttpResponse(json.dumps(result.data))
    response.status_code = 200
    response['Access-Control-Allow-Origin'] = '*'
    return response
