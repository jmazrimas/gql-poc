import graphene
from django.db import connection
from graphene_django.types import DjangoObjectType

from factory.models import Factory
from machine.models import Machine
from datasource.models import Datasource

# print('Factory NAME', Factory.objects.get(pk=1).machine_set.all()[0].name)
# print('Machine NAME', Machine.objects.get(pk=1).factory.name)
# print('Datasource NAME', Datasource.objects.get(pk=8).name)


class DatasourceType(DjangoObjectType):
    class Meta:
        model = Datasource

class FactoryType(DjangoObjectType):
    class Meta:
        model = Factory

#
# class Factory(graphene.ObjectType):
#     id = graphene.ID()
#     name = graphene.String()
#     # datasources = graphene.List(Datasource)
#     machines = graphene.List(Machine)
#
#     # def resolve_datasources(self, info):
#     #     cursor = connection.cursor()
#     #     query = "select d.id, d.name " \
#     #             "from machines m " \
#     #             "join datasources d on d.machine_id = m.key " \
#     #             "where m.factory_id={}".format(self.id)
#     #     cursor.execute(query, (), )
#     #
#     #     results = cursor.fetchall()
#     #     datasources = []
#     #     for datasource in results:
#     #         datasources.append(
#     #             Datasource(
#     #                 id=datasource[0],
#     #                 name=datasource[1],
#     #             )
#     #         )
#     #     return datasources


class Query(graphene.ObjectType):
    datasources = graphene.List(DatasourceType)
    factories = graphene.List(FactoryType)

    def resolve_datasources(self, info):
        # cursor = connection.cursor()
        # query = "select id, name from datasources"
        # cursor.execute(query, (), )
        #
        # results = cursor.fetchall()
        # datasources = []
        # for datasource in results:
        #     datasources.append(
        #         Datasource(
        #             id=datasource[0],
        #             name=datasource[1],
        #         )
        #     )
        # return datasources
        return Datasource.objects.all()

    def resolve_factories(self, info):
        # cursor = connection.cursor()
        # query = "select id, name from factory"
        # cursor.execute(query, (), )
        #
        # results = cursor.fetchall()
        # factories = []
        # for factory in results:
        #     factories.append(
        #         Datasource(
        #             id=factory[0],
        #             name=factory[1],
        #         )
        #     )
        # return factories
        return Factory.objects.all()