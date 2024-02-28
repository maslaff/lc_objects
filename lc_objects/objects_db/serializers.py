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


class ObjectSystemSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        "id_object_pk": "id_object__pk",
    }

    class Meta:
        model = Systems
        fields = "__all__"


class ObjectSystemCreateSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        "id_object_pk": "id_object__pk",
    }

    class Meta:
        model = Systems
        fields = ("id_system_type", "description", "documentation_path")
#        depth = 1


class ObjSysDeviceSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        "id_object_pk": "id_object__pk",
        "id_system_pk": "id_system__pk",
    }

    class Meta:
        model = None
        # fields = "__all__"
        exclude = []

    # def get_field_names(self, declared_fields, info):
    #     expanded_fields = super(ObjSysDeviceSerializer, self).get_field_names(
    #         declared_fields, info
    #     )

    #     if getattr(self.Meta, "extra_fields", None):
    #         return expanded_fields + self.Meta.extra_fields
    #     else:
    #         return expanded_fields


class ObjSysCreateDeviceSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        "id_object_pk": "id_object__pk",
        "id_system_pk": "id_system__pk",
    }

    class Meta:
        model = None
        fields = "__all__"


class SystemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemTypes
        fields = "__all__"


class SystemSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        "object_pk": "object__pk",
    }

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
        # depth = 1
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
    parent_lookup_kwargs = {
        "id_object_pk": "id_object__pk",
        "id_system_pk": "id_system__pk",
        "videorecorder_pk": "videorecorder__pk",
    }

    class Meta:
        model = CCTVCameras
        fields = "__all__"


class CCTVCameraCreateSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        "id_object_pk": "id_object__pk",
        "id_system_pk": "id_system__pk",
        "videorecorder_pk": "videorecorder__pk",
    }

    class Meta:
        model = CCTVCameras
        fields = (
            "cctv_system_type",
            "cctv_system_manufacturer",
            "model_name",
            "serial_number",
            "mac_address",
            "ip_address",
            "ip_mask",
            "admin_login",
            "admin_pass",
        )
