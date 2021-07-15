from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ProductListView, ProductViewSet #ProductListCreateView, ProductDetailView

# urlpatterns = [
#     path('list/', ProductListView.as_view(), name='listview'),
#     patch('list-create/', ProductListCreateView.as_view(), name='listcreateview'),
#     patch('{pk}/', ProductDetailView.as_view(), name='detailview'),
# ]

router = DefaultRouter()
router.register(r'', ProductViewSet, basename='productviewset')

urlpatterns = [
    path('viewer/', ProductListView.as_view(), name='productlistview'),
]

urlpatterns += router.urls