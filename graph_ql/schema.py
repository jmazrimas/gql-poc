import graphene
from django.db import connection


class Machine(graphene.ObjectType):
    id = graphene.ID()
    key = graphene.String()
    factory_id = graphene.Int()


class Factory(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()


class Datasource(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    machine = graphene.Field(Machine,)

    def resolve_machine(self, info):
        cursor = connection.cursor()
        query = "select m.id, m.key, m.factory_id " \
                "from machines m " \
                "join datasources d on d.machine_id = m.key " \
                "where d.id={}".format(self.id)
        cursor.execute(query, (), )

        results = cursor.fetchall()
        if len(results) > 0:
            print('RESULTS!!!!')
            return Machine(
                id=results[0][0],
                key=results[0][1],
                factory_id=results[0][2],
            )

        return None


class Query(graphene.ObjectType):
    datasources = graphene.List(Datasource)
    machine = graphene.Field(
        Machine,
        id=graphene.Int(),)

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

    def resolve_machine(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            cursor = connection.cursor()
            query = "select id, key, factory_id from machines where id={}".format(id)
            cursor.execute(query, (), )

            results = cursor.fetchall()
            machines = []
            for machine in results:
                machines.append(
                    Machine(
                        id=machine[0],
                        key=machine[1],
                        factory_id=machine[2],
                    )
                )

            return machines[0]

        return None
