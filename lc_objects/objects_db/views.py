from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# class PersonsList(generics.ListAPIView):
#     permission_classes = (IsAuthenticated,)

#     queryset = Persons.objects.all()
#     serializer_class = PersonSerializer


# class PersonCreate(generics.CreateAPIView):
#     permission_classes = (IsAuthenticated,)

#     queryset = Persons.objects.all()
#     serializer_class = PersonSerializer


# class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,)

#     queryset = Persons.objects.all()
#     serializer_class = PersonSerializer


class Perm:
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class PersonViewSet(Perm, viewsets.ModelViewSet):
    queryset = Persons.objects.all()
    serializer_class = PersonSerializer


class OrganizationsList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Organizations.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Organizations.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Organizations.objects.all()
    serializer_class = OrganizationSerializer
