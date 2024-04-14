
from django.contrib import admin
from ceremo_app.models import User,Profile,Category,Vendor,Item,ItemImages,Rental,RentalItem,ItemReview,Wishlist,Address

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','bio']


class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['user', 'full_name' ,'verified']

admin.site.register(User, UserAdmin)
admin.site.register( Profile,ProfileAdmin)



class ItemImagesAdmin(admin.TabularInline):
    model = ItemImages


class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImagesAdmin] 
    list_display = ['user','vendor','title', 'iid','item_image','category','price', 'featured', 'item_status','created_at','updated']
    



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']
   
class VendorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'vendor_image','date_created']
   


class RentalAdmin(admin.ModelAdmin):
    list_display = ['user',  'price', 'paid_status', 'item_status', 'booked_at', 'returned_at']
 



class RentalItemAdmin(admin.ModelAdmin):

    list_display = ['booking', 'item', 'price', 'invoice_no', 'image', 'quantity','total']
    


class ItemReviewAdmin(admin.ModelAdmin):
    list_display = ['item', 'user', 'rating', 'review']
   

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user','item','date']
 

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user','address','status']
    

# register these modles

admin.site.register(Category,CategoryAdmin )
admin.site.register(Vendor,VendorAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(Rental,RentalAdmin)
admin.site.register(RentalItem,RentalItemAdmin)
admin.site.register(ItemReview,ItemReviewAdmin)
admin.site.register(Wishlist,WishlistAdmin)
admin.site.register(Address,AddressAdmin)







