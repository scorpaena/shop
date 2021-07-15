from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from .models import Product
from .serializers import ProductSerializerEditor, ProductSerializerViewer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = ProductSerializerViewer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerEditor

    
    # def get_serializer_class(self):
    #     if self.request.user.is_staff:
    #         return ProductSerializerEditor
    #     return ProductSerializerViewer


# class ProductListCreateView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializerEditor


# class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializerEditor
