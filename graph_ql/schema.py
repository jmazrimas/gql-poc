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

class MachineType(DjangoObjectType):
    class Meta:
        model = Machine

class Query(graphene.ObjectType):
    datasources = graphene.List(DatasourceType)
    factories = graphene.List(FactoryType)
    machines = graphene.List(MachineType)

    def resolve_datasources(self, info):
        return Datasource.objects.all()

    def resolve_factories(self, info):
        return Factory.objects.all()

    def resolve_machines(self, info):
        return Machine.objects.all()
