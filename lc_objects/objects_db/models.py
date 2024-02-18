from django.db import models
from django.core.validators import RegexValidator


mac_regex = RegexValidator(
    regex=r"^(?:[a-fA-F0-9]{2}[ :-]?){5}[a-fA-F0-9]{2}$",
    message="Введите валидный MAC-адрес из шести пар символов, слитно, либо попарно разделенных пробелами/тире/двоеточием",
)


class Persons(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=80)
    phone_regex = RegexValidator(
        # regex=r"^(\+?7|8)?[ -(]?\d{3}?[ )]?(\d[ -]?){7}$",
        regex=r"^([+]?7|8)?([ -(]?\d{3}[ -)]?)((?:\d[ -]?){7})$",
        message="Введите Российский телефонный номер в формате 10 цифр: 9998887766. Подойдут любые общепринятые форматы записи телефонного номера",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)


class Organizations(models.Model):
    legal_name = models.CharField(max_length=100)
    legal_address = models.CharField(max_length=100)
    inn = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)


class LCObjects(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=120)
    organization_id = models.ForeignKey(Organizations, on_delete=models.CASCADE)
    contact_person = models.ManyToManyField(Persons)


class SystemTypes(models.Model):
    type_name = models.CharField(max_length=80)
    abbr = models.CharField(max_length=30)
    description = models.TextField()


class Systems(models.Model):
    id_object = models.ForeignKey(LCObjects, on_delete=models.CASCADE)
    id_system_type = models.ForeignKey(SystemTypes, on_delete=models.CASCADE)
    description = models.TextField()
    documentation_path = models.FileField()


# ---------------------- FAS / ALR


class ManufacturerFSS(models.Model):
    name = models.CharField(max_length=50)


class TypeFSS(models.Model):
    name = models.CharField(max_length=50)


class ControlPanelModels(models.Model):
    class Meta:
        # for naming you table
        db_table = "Модели ППКОП"

    model_name = models.CharField(max_length=50)
    type_id = models.ForeignKey(TypeFSS, on_delete=models.CASCADE)
    aps_system_manufacturer_id = models.ForeignKey(
        ManufacturerFSS, on_delete=models.CASCADE
    )


class ControlPanels(models.Model):
    model = models.ForeignKey(
        ControlPanelModels, verbose_name=("ППКОП"), on_delete=models.CASCADE
    )
    admin_pass = models.CharField(max_length=30)
    operator_pass = models.CharField(max_length=30)
    serial_number = models.CharField(max_length=50)
    hw_version = models.CharField(max_length=50)
    sw_version = models.CharField(max_length=50)
    configuration_file = models.FileField()


# ---------------------- LAN/SCS


class NetDevManufacturers(models.Model):
    name = models.CharField(max_length=50)


class NetDevTypes(models.Model):
    name = models.CharField(max_length=50)


class NWD_Models(models.Model):
    class Meta:
        # for naming you table
        db_table = "Модели сетевых устройств"

    id_system = models.ForeignKey(Systems, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=50)
    type_id = models.ForeignKey(NetDevTypes, on_delete=models.CASCADE)
    nwd_manufacturer_id = models.ForeignKey(
        NetDevManufacturers, on_delete=models.CASCADE
    )


class NetworkDevices(models.Model):
    id_system = models.ForeignKey(Systems, on_delete=models.CASCADE)
    id_network_device_model = models.ForeignKey(NWD_Models, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    mac_address = models.CharField(validators=[mac_regex], max_length=50, blank=True)
    configuration_file = models.FileField()
    ip_address = models.GenericIPAddressField(protocol="IPv4")
    ip_mask = models.GenericIPAddressField(protocol="IPv4")
    admin_login = models.CharField(max_length=50)
    admin_pass = models.CharField(max_length=50)


# ---------------------- CCTV


class CCTVManufacturers(models.Model):
    name = models.CharField(max_length=50)


class CCTVTypes(models.Model):
    name = models.CharField(max_length=50)


class CCTVRecorders(models.Model):
    model = models.CharField(max_length=50)
    admin_login = models.CharField(max_length=50)
    admin_pass = models.CharField(max_length=50)
    ip_address = models.GenericIPAddressField(protocol="IPv4")
    ip_mask = models.GenericIPAddressField(protocol="IPv4")
    mac_address = models.CharField(validators=[mac_regex], max_length=50, blank=True)
    serial_number = models.CharField(max_length=50)
    id_cctv_system_manufacturer = models.ForeignKey(
        CCTVManufacturers, on_delete=models.CASCADE
    )
    id_cctv_system_type = models.ForeignKey(CCTVTypes, on_delete=models.CASCADE)
    id_system = models.ForeignKey(Systems, on_delete=models.CASCADE)


class CCTVCameras(models.Model):
    id_cctv_system_type = models.ForeignKey(CCTVTypes, on_delete=models.CASCADE)
    id_cctv_system_manufacturer = models.ForeignKey(
        CCTVManufacturers, on_delete=models.CASCADE
    )
    id_videorecorder = models.ForeignKey(CCTVRecorders, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    mac_address = models.CharField(validators=[mac_regex], max_length=50, blank=True)
    ip_address = models.GenericIPAddressField(protocol="IPv4")
    ip_mask = models.GenericIPAddressField(protocol="IPv4")
    admin_login = models.CharField(max_length=50)
    admin_pass = models.CharField(max_length=50)
