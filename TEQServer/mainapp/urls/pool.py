from django.urls import path

from mainapp.views.pool import PoolRetrieveAPIView, CategoryCreateAPIView, CategoryUpdateDestroyAPIView, ItemCreateAPIView, \
    ItemUpdateDestroyAPIView

urlpatterns = [
    path("pool/", PoolRetrieveAPIView.as_view()),
    path("category/", CategoryCreateAPIView.as_view()),
    path("category/<str:pk>/", CategoryUpdateDestroyAPIView.as_view()),
    path("category/<str:category_id>/item/", ItemCreateAPIView.as_view()),
    path("category/<str:pk>/item/<int:index>", ItemUpdateDestroyAPIView.as_view()),
]
