from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product
from .serializers import ProductEditorSerializer, ProductViewerSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return ProductEditorSerializer
        return ProductViewerSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductEditorSerializer
