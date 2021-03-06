from copyreg import constructor
from struct import pack
from django.contrib import messages
from django.db.models.query import QuerySet
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from rest_framework.serializers import Serializer
from users import serializers

from users.serializers import CartSerializer, CategorySerializer, PackageItemSerializer, PackagesSerializer, ProductSerializer, UserProfileSerializer, UserSerializer
from users.models import Category, Location, PackageItems, Package, Products, Cart, Purchase, UserProfile

from django.contrib.auth.decorators import login_required

from rest_framework.authtoken.models import Token

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.pagination import DjangoPaginator, PageNumberPagination
from rest_framework import generics, status
from django.db.models import Q

@api_view(['GET', 'POST'])
def all_users(request):
    if (request.method == 'GET'):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([])
def productDetails(request, slug):
    if request.method == 'GET':
        try:
            product = Products.objects.get(slug=slug)
            serializer = ProductSerializer(product)
            data = serializer.data
        except:
            data = []
        return Response(data)

# @login_required(login_url='rest-auth/')
@api_view(['GET'])
#@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def carts(request):
    if request.method == 'GET':
        user = User.objects.get(username=request.user)
        try:
            cartItems = Cart.objects.filter(user=user)
            serializer = CartSerializer(cartItems, many=True)
            data = serializer.data
        except:
            data = {}

        return Response(data)

@api_view(['GET'])
# @authentication_classes([SessionAuthentication])
@permission_classes([])
def hello(request):
    user = str(request.user)
    return Response({'hello': user})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addToCart(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        cartItems = request.data
        for cartItem in cartItems:
            product = Products.objects.get(id=cartItem.get('product'))
            quantity = cartItem.get('quantity')
            
            cart = Cart.objects.filter(Q(user=user) & Q(product=product))
            if cart.exists():
                cart.update(quantity=quantity)
            else:
                cart = Cart(user=user, product=product, quantity=quantity)
                cart.save()
            print(cart)
    
        return Response(request.data)



class StandardResultsSetPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ProductsList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []
    pagination_class = StandardResultsSetPagination

class GetItemsByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = []
    pagination_class = StandardResultsSetPagination

    def get(self, request, pk, *args, **kwargs):
        self.pk = pk
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        category = Category.objects.get(id=self.pk)
        products = Products.objects.filter(category=category)
        return products

@api_view(['GET'])
@permission_classes([])
def allCategories(request):
    if (request.method == 'GET'):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout(request):
    purchase = Purchase()
    user = User.objects.get(username=request.user)
    deliveryLoc = Location()
    deliveryLoc.description = request.data.get('location').get('description')
    deliveryLoc.latitude = request.data.get('location').get('latitude')
    deliveryLoc.longitude = request.data.get('location').get('longitude')
    deliveryLoc.save()
    items = Cart.objects.filter(user=user)
    
    for item in items:
        purchase.product = Products.objects.get(name=item.product)
        purchase.quantity = item.quantity
        purchase.user = user
        purchase.deliveryLocation = deliveryLoc
        purchase.save()
        item.delete()
    
    return Response(request.data)

@api_view(['GET'])
@permission_classes([])
def packages(request):
    packages = Package.objects.all()
    data = {}
    for package in packages:
        packId = package.id
        item = {}
        item['name'] = str(package.name)
        item['description'] = package.description
        packageItems = PackageItems.objects.filter(package=package)
        packageItemSerializer = PackageItemSerializer(packageItems, many=True)
        item['items'] = packageItemSerializer.data
        data[packId] = item
    return Response(data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteAccount(request):
    user = User.objects.get(username=request.user)
    user.delete()
    return Response(status=status.HTTP_200_OK)
