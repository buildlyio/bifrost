import logging
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets
from core.models import Consortium
from core.serializers import ConsortiumSerializer
from core.permissions import IsSuperUser, AllowAuthenticatedRead
logger = logging.getLogger(__name__)


class ConsortiumViewSet(viewsets.ModelViewSet):
    """
    Consortium is group of custodians that enables sharing of data.

    title:
    Consortium

    description:
    A Consortium is collective group of custodians

    which are in turn associated with an organization.

    retrieve:
    Return the Consortium.

    list:
    Return a list of all the existing Consortiums.

    create:
    Create a new Consortium instance.

    update:
    Update a Consortium instance.

    delete:
    Delete a Consortium instance.
    """
    permission_classes_by_action = {'list': [AllowAuthenticatedRead]}

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        organization_uuid = self.request.query_params.get('organization_uuid', None)
        # It will check if organization uuid in query param
        if organization_uuid is not None:
            queryset = queryset.filter(organization_uuids__contains=[organization_uuid])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
<<<<<<< HEAD
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
=======
            return [permission() for permission in self.permission_classes_by_action[self.action]]
>>>>>>> master
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

    filter_fields = ('name',)
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsSuperUser,)
    queryset = Consortium.objects.all()
    serializer_class = ConsortiumSerializer
