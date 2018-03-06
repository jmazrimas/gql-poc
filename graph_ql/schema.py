import graphene
from django.db import connection


class Machine(graphene.ObjectType):
    id = graphene.ID()
    key = graphene.String()
    factory_id = graphene.Int()


class Datasource(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    machine = graphene.Field(Machine,)
    # factory = graphene.Field(Factory, )

    def resolve_machine(self, info):
        cursor = connection.cursor()
        query = "select m.id, m.key, m.factory_id " \
                "from machines m " \
                "join datasources d on d.machine_id = m.key " \
                "where d.id={}".format(self.id)
        cursor.execute(query, (), )

        results = cursor.fetchall()
        if len(results) > 0:
            return Machine(
                id=results[0][0],
                key=results[0][1],
                factory_id=results[0][2],
            )

        return None

    # def resolve_factory(self, info):
    #     cursor = connection.cursor()
    #     query = "select f.id, f.name " \
    #             "from machines m " \
    #             "join datasources d on d.machine_id = m.key " \
    #             "join factory f on m.factory_id = f.id " \
    #             "where d.id={}".format(self.id)
    #     cursor.execute(query, (), )
    #
    #     results = cursor.fetchall()
    #     if len(results) > 0:
    #         return Factory(
    #             id=results[0][0],
    #             name=results[0][1],
    #         )
    #
    #     return None


class Factory(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    datasources = graphene.List(Datasource)

    def resolve_datasources(self, info):
        print('RESOLVE MACHINES')
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
                Machine(
                    id=datasource[0],
                    name=datasource[1],
                )
            )
        return datasources


class Query(graphene.ObjectType):
    datasources = graphene.List(Datasource)
    factories = graphene.List(Factory)
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
