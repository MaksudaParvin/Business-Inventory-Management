from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Company, User
from .serializers import CompanySerializer, UserSerializer
from .permissions import IsAdmin

class CompanyViewSet(viewsets.ModelViewSet):

    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    queryset = Company.objects.all()


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(
            company=self.request.user.company
        )

    def get_permissions(self):

        if self.action in ['create', 'destroy', 'update', 'partial_update',]:
            permission_classes = [IsAuthenticated, IsAdmin]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(
            company=self.request.user.company
        )