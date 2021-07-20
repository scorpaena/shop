from rest_framework import generics
from user.permissions import IsViewer
from .models import Product
from .serializers import ProductEditorSerializer, ProductViewerSerializer


class ProductEditorView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductEditorSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductEditorSerializer


class ProductViewerView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductViewerSerializer
    permission_classes = [
        IsViewer,
    ]
