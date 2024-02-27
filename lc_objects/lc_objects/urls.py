from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("lc/", include("objects_db.urls")),
] # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

