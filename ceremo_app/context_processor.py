from ceremo_app.models import User,Profile,Category,Vendor,Item,ItemImages,Rental,RentalItem,ItemReview,Wishlist,Address

def default(request):
    categories = Category.objects.all()
    try:
        address = Address.objects.get(user=request.user)
    except:
        address = None

    return {
        'categories': categories,
        'address': address

            }
    