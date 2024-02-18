from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"persons", views.PersonViewSet, basename="person")
urlpatterns = router.urls

urlpatterns += [
    path("token-auth/", obtain_auth_token),
    # path("persons/", views.PersonsList.as_view(), name="Person list"),
    # path("persons/add/", views.PersonCreate.as_view(), name="Person create"),
    # path("persons/<int:pk>", views.PersonDetail.as_view(), name="Person view and edit"),
    # path("users/", views.users, name="users"),
    # path("products/", views.products, name="products"),
    # path("user/<int:client_id>", views.orders_list, name="orders_list"),
    # path(
    #     "user/<int:client_id>/prods/<str:period>",
    #     views.userorders_product_list,
    #     name="userorders_product_list_from",
    # ),
    # path(
    #     "user/<int:client_id>/prods/",
    #     views.userorders_product_list,
    #     name="userorders_product_list",
    # ),
    # path("product/<int:product_id>", views.product_form, name="product_edit"),
]
