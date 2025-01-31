from django.urls import path
from . import views

urlpatterns = [
    # path('<int:pk>/',views.ProductDetailAPIView.as_view(),name="Product details"),

    path('',views.list_product_create_view),
    # path('',views.product_create_view),

    # @apiView
    # path('',views.product_alt_view),
    path('<int:pk>/update/',views.list_product_update_view),
    path('<int:pk>/delete/',views.product_delete_view),
    # path('<int:pk>/',views.product_alt_view),

    #mixins
    # path('',views.product_mixin_view),
    # path('<int:pk>/',views.product_mixin_view),


]
