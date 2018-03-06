import graphene
# from django.db import connection


class Datasource(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()


class Query(graphene.ObjectType):
    datasources = graphene.String(description='A typical hello world')
    hello = graphene.String(description='A typical hello world')

    def resolve_datasources(self, info):
        print('RESOLVE DATASOURCES')
        # return [{
        #     "id": 99,
        #     "name": "fake machine",
        # }]
        return "datasources string II"

    def resolve_hello(self, info):
        return 'World'