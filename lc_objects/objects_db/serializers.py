from rest_framework import serializers
from .models import *


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = "__all__"


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = "__all__"


class LCObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = LCObjects
        fields = "__all__"


class SystemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemTypes
        fields = "__all__"


class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Systems
        fields = "__all__"


class ManufacturerFSSSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManufacturerFSS
        fields = "__all__"


class TypeFSSSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeFSS
        fields = "__all__"


class ControlPanelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlPanelModels
        fields = "__all__"


class ControlPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlPanels
        fields = "__all__"


class NetDevManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetDevManufacturers
        fields = "__all__"


class NetDevTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetDevTypes
        fields = "__all__"


class NWD_ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NWD_Models
        fields = "__all__"


class NetworkDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkDevices
        fields = "__all__"


class CCTVManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCTVManufacturers
        fields = "__all__"


class CCTVTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCTVTypes
        fields = "__all__"


class CCTVRecorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCTVRecorders
        fields = "__all__"


class CCTVCameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCTVCameras
        fields = "__all__"
