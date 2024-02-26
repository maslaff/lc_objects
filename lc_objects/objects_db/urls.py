from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_nested import routers
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"persons", views.PersonViewSet)
router.register(r"orgs", views.OrganizationViewSet)
router.register(r"systypes", views.SystemTypeViewSet)

router.register(r"seqursys/manufacturers", views.ManufacturerFSSViewSet)
router.register(r"seqursys/types", views.TypeFSSViewSet)
router.register(r"seqursys/models", views.ControlPanelModelViewSet)
router.register(r"lansys/manufacturers", views.NetDevManufacturerViewSet)
router.register(r"lansys/types", views.NetDevTypeViewSet)
router.register(r"lansys/models", views.NWD_ModelViewSet)
router.register(r"cctvsys/manufacturers", views.CCTVManufacturerViewSet)
router.register(r"cctvsys/types", views.CCTVTypeViewSet)
# router.register(r"cctvsys/models", views.CCTVRecorderViewSet)

router.register(r"lcobjects", views.LCObjectViewSet, basename="lcobjects")

obj_system_router = routers.NestedSimpleRouter(router, r"lcobjects", lookup="id_object")
obj_system_router.register(r"systems", views.ObjectSystemViewSet, basename="systems")

objsys_device_router = routers.NestedSimpleRouter(
    obj_system_router, r"systems", lookup="id_system"
)
objsys_device_router.register(r"devices", views.ObjSysDeviceViewSet, basename="devices")

cameras_router = routers.NestedSimpleRouter(
    objsys_device_router, r"devices", lookup="videorecorder"
)
cameras_router.register(r"cameras", views.CamerasViewSet, basename="cameras")


urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path("token-auth/", obtain_auth_token),
    path(r"", include(router.urls)),
    path(r"", include(obj_system_router.urls)),
    path(r"", include(objsys_device_router.urls)),
    path(r"", include(cameras_router.urls)),
]
