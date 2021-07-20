from django.urls import path
from .views import ProductEditorView, ProductViewerView, ProductDetailView

urlpatterns = [
    path("editor/", ProductEditorView.as_view(), name="producteditorview"),
    path("editor/<int:pk>/", ProductDetailView.as_view(), name="productdetailview"),
    path("viewer/", ProductViewerView.as_view(), name="productviewerview"),
]
