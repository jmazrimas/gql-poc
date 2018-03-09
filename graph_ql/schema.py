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

    datasources = graphene.List(DatasourceType)

    def resolve_datasources(self, info):
        machines = Machine.objects.filter(factory_id=self.id)
        return Datasource.objects.all().filter(machine__in=machines)
        # return Datasource.objects.all()


class MachineType(DjangoObjectType):
    class Meta:
        model = Machine


class Query(graphene.ObjectType):
    # valid query params are defined here:
    datasources = graphene.List(DatasourceType, id=graphene.Int())
    factories = graphene.List(FactoryType, id=graphene.Int(), name=graphene.String())
    machines = graphene.List(MachineType, id=graphene.Int())

    def resolve_datasources(self, info, **kwargs):
        return Datasource.objects.all().filter(**kwargs)

    def resolve_factories(self, info, **kwargs):
        return Factory.objects.all().filter(**kwargs)

    def resolve_machines(self, info, **kwargs):
        return Machine.objects.all().filter(**kwargs)
