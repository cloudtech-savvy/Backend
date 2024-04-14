
from taggit.models import Tag
from django.db.models import Count, Avg
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.response import Response
from ceremo_app.models import User
from ceremo_app.serializers import  MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import login, authenticate, logout
from  ceremo_app.forms import UserRegisterForm
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

from ceremo_app.models import User,Profile,Category,Vendor,Item,ItemImages,Rental,RentalItem,ItemReview,Wishlist,Address


# user=settings.AUTH_USER_MODEL

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = ([AllowAny])
    serializer_class = RegisterSerializer

# Uesr Homepage view

def homepage_view(request):
    name='homepage'
    context = {
        name: 'homepage'
    }
    return render(request, 'index.html', context)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    if request.method == 'GET':
        response = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': response}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        response = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': response}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


# user registration view

def register_View(request):
    if  request.method == 'POST':
       return render(request, 'hi',)
    # if request.method == 'POST':
    #     form = UserRegisterForm(request.POST)
    #     if form.is_valid():
    #         new_user = form.save()
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'Hey {username}, your account has been created successfully!')
    #         new_user = authenticate(username=form.cleaned_data['username'],
    #                                 password=form.cleaned_data['password1'],
    #                                 )
    #         # Login the new user
    #         login(request, new_user)
    #         return redirect('homepage')  # Make sure 'dashboard:' is a valid URL name
    # else:
    #     form = UserRegisterForm() 
    # context = {'form': form}   
    # return render(request, 'signup.html', context)

  
#user login view
def login_view(request):    
    if request.user.is_authenticated:  
        return redirect('homepage')
    
def login_view(request):    
    if request.user.is_authenticated:  
        return redirect('homepage')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
      
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
    
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('homepage')
            else:
                messages.warning(request, 'Incorrect password. Please try again.')
            
        except User.DoesNotExist:
            messages.warning(request, f'User with {email} does not exist!')
            return redirect('login')

    return render(request, 'signin.html')     

#user logout view
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')

    return redirect('homepage')#redirect use where you want
    # return redirect("templates:sign-in")#redirect use where you want


################ views for isting all items,we have in our database ####################
def item_list_view(request):
    # items = Item.objects.all().order_by('-created_at')
    # items = Item.filter(status='published').order_by('-created_at')
    items = Item.objects.filter(category='1').order_by('-created_at')
    return render(request, 'item_list.html', {'items': items})

 ##################views for fetcing item details####################

def item_detail_view(request, iid):
    item = Item.objects.get(iid=iid)
    item_image = Item.i_images.all()
    items=Item.objects.filter(category=item.category).exclude(iid=iid).order_by('-created_at')[:4]

    ########## getting Item reviews ##########

    reviews=ItemReview.objects.filter(item=item).order_by('-created_at')

    ########################### getting average rating ####################

    avg_rating=ItemReview.objects.filter(item=item).aggregate(rating=Avg('rating'))


    context={
        'item':item,
        'item_image':item_image,
        'items':items,
        'reviews':reviews,
        'avg_rating':avg_rating
    }
    return render(request, 'item_detail.html',context)

############   views for category list ###############

def category_list_view(request):
    # category = Category.objects.all()
    #count all items in each category   
    categories = Category.objects.annotate(item_count=Count('item')).order_by('title')
    return render(request, 'category_list.html', {'category': categories}) 

################### create item catogory  list view  ####################

def item_category_list_view(request,cid):
    category = Category.objects.get(cid=cid) 

    items=Item.objects.filter(item_status='published',category=category).order_by('-created_at')

    context={
        'category':category,
        'items':items
    }
    return render(request, 'category_list.html', {'category': context})
############### views for vendor list ####################

def vendor_list_view(request):
    vendors = Vendor.objects.all()

    context={
        'vendors':vendors
    }
    return render(request,'vendor_list.html', {'vendors': context})

################## views for fetching vendor details ####################

def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    items=Item.objects.filter(vendor=vendor).order_by('-created_at',item_status='published')

    context={
        'vendor':vendor,
        'items':items,
    }

    return render(request, 'vendor_detail.html', context)

##################### functionality for tags ####################

def tag_list_view(request, tag_slug=None):
    items = Item.objects.filter( item_status='published').order_by('-created_at')
    tag=None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        items = items.filter(tags__in=[tag])
        
        context={
            'tag':tag,
            'items':items
        }
    return render(request, 'tag_list.html', context)