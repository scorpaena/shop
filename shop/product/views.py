from rest_framework import generics
from user.permissions import IsEditor
from .models import Product
from .serializers import ProductEditorSerializer, ProductViewerSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.user.groups.filter(name='editors').exists():
            return ProductEditorSerializer
        return ProductViewerSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductEditorSerializer
    permission_classes = [IsEditor,]
