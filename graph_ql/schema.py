import graphene
from django.db import connection


class Datasource(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()


class Factory(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    datasources = graphene.List(Datasource)

    def resolve_datasources(self, info):
        cursor = connection.cursor()
        query = "select d.id, d.name " \
                "from machines m " \
                "join datasources d on d.machine_id = m.key " \
                "where m.factory_id={}".format(self.id)
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


class Query(graphene.ObjectType):
    datasources = graphene.List(Datasource)
    factories = graphene.List(Factory)

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

    def resolve_factories(self, info):
        cursor = connection.cursor()
        query = "select id, name from factory"
        cursor.execute(query, (), )

        results = cursor.fetchall()
        factories = []
        for factory in results:
            factories.append(
                Datasource(
                    id=factory[0],
                    name=factory[1],
                )
            )
        return factories