from django.urls import path
from . import views

urlpatterns = [
    # path('<int:pk>/',views.ProductDetailAPIView.as_view(),name="Product details"),
    # path('',views.product_create_view)
    # path('',views.list_product_create_view)
    path('',views.product_alt_view),
    path('<int:pk>/',views.product_alt_view)
]
