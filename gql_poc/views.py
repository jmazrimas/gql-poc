from django.http import HttpResponse
import json


def index(request):
    """
    :param request:
    :return: a list of all factories, no filtering (yet)
    """

    # cursor = connection.cursor()
    # query = "select id, name, created_at from factory order by id"
    # cursor.execute(query, (),)
    #
    # results = cursor.fetchall()
    # factory_obj = []
    # for factory in results:
    #     factory_obj.append({
    #         'id': factory[0],
    #         'name': factory[1],
    #         'created_at': str(factory[2])
    #     })

    response = HttpResponse(json.dumps({"a key": "a value"}))
    response.status_code = 200
    response['Access-Control-Allow-Origin'] = '*'
    return response
