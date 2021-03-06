from users import views
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('users', views.all_users),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('product/<str:slug>/', views.productDetails, name='product'),
    path('cart/', views.carts, name='cart'),
    path('hello/', views.hello, name='hello'),
    path('addtocart/', views.addToCart, name='addToCart'),
    path('products/', views.ProductsList.as_view(), name='products'),
    path('categories/', views.allCategories, name="allCategories"),
    path('itemsbycategory/<str:pk>/', views.GetItemsByCategory.as_view(), name="getItemsByCategory"),
    path('checkout/', views.checkout, name="checkout"),
    path('packages/', views.packages, name='packages'),
    path('deleteAccount', views.deleteAccount, name='deleteAccount'),

]