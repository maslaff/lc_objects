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
    # serializer_class = ObjectSystemSerializer
    def get_serializer_class(self):
        print("\n\nGET_SERIALIZER\n\n")
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
        print(kwargs)
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
        request.data._mutable = True
        data = request.data
        data["videorecorder"] = self.kwargs["videorecorder_pk"]
        serializer = CCTVCameraSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError:
            return Response(
                {"errors": (serializer.errors,)}, status=status.HTTP_400_BAD_REQUEST
            )


# class ObjectSystemViewSet(Perm, viewsets.ViewSet):
#     serializer_class = ObjectSystemSerializer

#     def list(self, request, id_object_pk=None):
#         queryset = Systems.objects.filter(id_object=id_object_pk)
#         print(queryset)
#         serializer = ObjectSystemSerializer(
#             queryset, many=True, context={"request": request}
#         )
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None, id_object_pk=None):
#         queryset = Systems.objects.filter(pk=pk, id_object=id_object_pk)
#         syst = get_object_or_404(queryset, pk=pk)
#         serializer = ObjectSystemSerializer(syst, context={"request": request})
#         return Response(serializer.data)

#     def create(self, request, id_object_pk=None):
#         serializer = ObjectSystemCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             snew = Systems(
#                 id_object=id_object_pk,
#                 id_system_type=serializer.validated_data["id_system_type"],
#                 description=serializer.validated_data["description"],
#                 documentation_path=serializer.validated_data["documentation_path"],
#             )
#             snew.save()
#             return Response({"status": "System added"})
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ObjectSystemViewSet(Perm, viewsets.ModelViewSet):
#     queryset = Systems.objects.filter(id_object=obj)
#     serializer_class = ObjectSystemSerializer


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


"""
{'cctv_system_manufacturer': NestedSerializer(read_only=True):
    id = IntegerField(label='ID', read_only=True)
    name = CharField(max_length=50), 
'cctv_system_type': NestedSerializer(read_only=True):
    id = IntegerField(label='ID', read_only=True)
    name = CharField(max_length=50), 
'admin_pass': CharField(max_length=50), 
'ip_mask': IPAddressField(validators=[<function validate_ipv4_address>]), 
'serial_number': CharField(max_length=50), 
'admin_login': CharField(max_length=50), 
'mac_address': CharField(allow_blank=True, max_length=50, required=False, validators=[<django.core.validators.RegexValidator object>]), 
'ip_address': IPAddressField(validators=[<function validate_ipv4_address>]), 
'id': IntegerField(label='ID', read_only=True), 
'model': CharField(max_length=50)}
"""
