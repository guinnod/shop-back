from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


@api_view(['GET'])
def getAllCategory(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCategory(request, id):
    try:
        category = Category.objects.get(pk=id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    except:
        return Response(status=400)


@api_view(['GET'])
def getAllProduct(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, id):
    try:
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except:
        return Response(status=400)


@api_view(['GET'])
def getProductsByCategory(request, id):
    try:
        category = Category.objects.get(pk=id)
        category_name = category.name
        product = Product.objects.filter(description=category_name)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    except:
        return Response(status=400)
