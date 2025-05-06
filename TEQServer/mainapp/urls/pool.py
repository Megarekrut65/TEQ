from django.urls import path

from mainapp.views.pool import PoolRetrieveAPIView, CategoryCreateAPIView, CategoryUpdateDestroyAPIView, ItemCreateAPIView, \
    ItemUpdateDestroyAPIView

urlpatterns = [
    path("pool/", PoolRetrieveAPIView.as_view()),
    path("category/", CategoryCreateAPIView.as_view()),
    path("category/<str:pk>/", CategoryUpdateDestroyAPIView.as_view()),
    path("category/item/<str:category_id>/", ItemCreateAPIView.as_view()),
    path("category/item/<int:index>/<str:pk>/", ItemUpdateDestroyAPIView.as_view()),
]
