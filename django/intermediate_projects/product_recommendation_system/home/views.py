from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .product_recommender import get_similar_products

def index(request):
    return render(request, 'index.html')

def product_detail(request, id):
    context = {'id': id}
    return render(request, 'product_detail.html', context)


# Create your views here.
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all().order_by('?')[:40]
        serializer = ProductSerializer(products, many=True)
        return Response({
            'all_products': serializer.data
        })
    
class ProductDetailView(APIView):
    def get(self, request,id):
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product)
        similar_products= get_similar_products(id,10)
        similar_products_serializer=ProductSerializer(similar_products,many=True)
        return Response({
            'product': serializer.data,
            "similar_products": similar_products_serializer.data
        })
