from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.response import Response
from django.utils.module_loading import import_string
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import ValidationError
from rest_framework import status


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


class OrganizationViewSet(Perm, viewsets.ModelViewSet):
    queryset = Organizations.objects.all()
    serializer_class = OrganizationSerializer


class LCObjectViewSet(Perm, viewsets.ModelViewSet):
    queryset = LCObjects.objects.all()
    serializer_class = LCObjectSerializer


class ObjectSystemViewSet(Perm, viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action in ("create", "update"):
            return ObjectSystemCreateSerializer
        return ObjectSystemSerializer

    def get_queryset(self):
        return Systems.objects.filter(id_object=self.kwargs["id_object_pk"])

    def create(self, request, *args, **kwargs):
        data = request.data
        data["id_object"] = self.kwargs["id_object_pk"]
        serializer = ObjectSystemSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError:
            return Response(
                {"errors": (serializer.errors,)}, status=status.HTTP_400_BAD_REQUEST
            )


class ObjSysDeviceViewSet(Perm, viewsets.ModelViewSet):
    def dispatch(self, request, *args, **kwargs):
        stype_obj = (
            Systems.objects.filter(pk=kwargs["id_system_pk"]).first().id_system_type
        )
        stype = stype_obj.table
        self.device_model = import_string(f"objects_db.models.{stype}")

        return super(ObjSysDeviceViewSet, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.device_model.objects.filter(system_id=self.kwargs["id_system_pk"])

    def get_serializer_class(self):
        serializer = ObjSysDeviceSerializer
        serializer.Meta.model = self.device_model
        serializer.Meta.exclude = []

        if self.action == "create":
            serializer.Meta.exclude = ["system"]
        return serializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["system"] = self.kwargs["id_system_pk"]
        ObjSysDeviceSerializer.Meta.exclude = []
        serializer = ObjSysDeviceSerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError:
            return Response(
                {"errors": (serializer.errors,)}, status=status.HTTP_400_BAD_REQUEST
            )


class CamerasViewSet(Perm, viewsets.ModelViewSet):
    def dispatch(self, request, *args, **kwargs):
        stype_obj = (
            Systems.objects.filter(pk=kwargs["id_system_pk"]).first().id_system_type
        )
        if stype_obj.table != "CCTVRecorders":
            raise Exception("У этого нет камер")

        return super(CamerasViewSet, self).dispatch(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action in ("create", "update"):
            return CCTVCameraCreateSerializer
        return CCTVCameraSerializer

    def get_queryset(self):
        return CCTVCameras.objects.filter(videorecorder=self.kwargs["videorecorder_pk"])

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["videorecorder"] = self.kwargs["videorecorder_pk"]
        serializer = CCTVCameraSerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError:
            return Response(
                {"errors": (serializer.errors,)}, status=status.HTTP_400_BAD_REQUEST
            )


class SystemTypeViewSet(Perm, viewsets.ModelViewSet):
    queryset = SystemTypes.objects.all()
    serializer_class = SystemTypeSerializer


class SystemViewSet(Perm, viewsets.ModelViewSet):
    queryset = Systems.objects.all()
    serializer_class = SystemSerializer


class ManufacturerFSSViewSet(Perm, viewsets.ModelViewSet):
    queryset = ManufacturerFSS.objects.all()
    serializer_class = ManufacturerFSSSerializer


class TypeFSSViewSet(Perm, viewsets.ModelViewSet):
    queryset = TypeFSS.objects.all()
    serializer_class = TypeFSSSerializer


class ControlPanelModelViewSet(Perm, viewsets.ModelViewSet):
    queryset = ControlPanelModels.objects.all()
    serializer_class = ControlPanelModelSerializer


class NetDevManufacturerViewSet(Perm, viewsets.ModelViewSet):
    queryset = NetDevManufacturers.objects.all()
    serializer_class = NetDevManufacturerSerializer


class NetDevTypeViewSet(Perm, viewsets.ModelViewSet):
    queryset = NetDevTypes.objects.all()
    serializer_class = NetDevTypeSerializer


class NWD_ModelViewSet(Perm, viewsets.ModelViewSet):
    queryset = NWD_Models.objects.all()
    serializer_class = NWD_ModelSerializer


class CCTVManufacturerViewSet(Perm, viewsets.ModelViewSet):
    queryset = CCTVManufacturers.objects.all()
    serializer_class = CCTVManufacturerSerializer


class CCTVTypeViewSet(Perm, viewsets.ModelViewSet):
    queryset = CCTVTypes.objects.all()
    serializer_class = CCTVTypeSerializer


class CCTVRecorderViewSet(Perm, viewsets.ModelViewSet):
    queryset = CCTVRecorders.objects.all()
    serializer_class = CCTVRecorderSerializer
