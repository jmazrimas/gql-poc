import graphene
from django.db import connection
from graphene_django.types import DjangoObjectType

from factory.models import Factory
from machine.models import Machine
from datasource.models import Datasource


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
    factories = graphene.List(FactoryType, id=graphene.Int(), name=graphene.String())
    machines = graphene.List(MachineType)

    def resolve_datasources(self, info, **kwargs):
        return Datasource.objects.all().filter(**kwargs)

    def resolve_factories(self, info, **kwargs):
        return Factory.objects.all().filter(**kwargs)

    def resolve_machines(self, info, **kwargs):
        return Machine.objects.all().filter(**kwargs)
