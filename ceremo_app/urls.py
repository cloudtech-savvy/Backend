from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # Add this import
from .views import MyTokenObtainPairView, RegisterView,register_View,login_view,homepage_view,logout_view,item_list_view,item_detail_view,category_list_view,item_category_list_view, tag_list_view,vendor_list_view,vendor_detail_view

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Import TokenRefreshView
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('home/', homepage_view, name='homepage'),
    path('signup/', register_View, name='sign-up'),
    path('sign-in/', login_view, name='sign-in'),
    path('sign-out/', logout_view, name='sign-out'),
    path('items/', item_list_view, name='items'),
    path('items/<iid>/', item_detail_view, name='items'),
    path('category/', category_list_view, name='categories'),
    path('category/<cid>/', item_category_list_view, name='item_category_list'),
    path('vendor/', vendor_list_view, name='vendors-list'),
    path('vendor/<vid>/',vendor_detail_view, name='vendors-detail'),
    path('items/tag/<slug:tag>/',tag_list_view, name='tagged_items')
]
