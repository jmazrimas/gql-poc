import graphene
from django.db import connection


class Datasource(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()


class Query(graphene.ObjectType):
    datasources = graphene.List(Datasource)

    def resolve_datasources(self, info):
        cursor = connection.cursor()
        query = "select id, name from datasources"
        cursor.execute(query, (), )

        results = cursor.fetchall()
        datasources = []
        for datasource in results:
            datasources.append(
                Datasource(
                    id=datasource[0],
                    name=datasource[1],
                )
            )

        return datasources