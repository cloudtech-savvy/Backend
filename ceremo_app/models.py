from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from shortuuidfield import ShortUUIDField
from django.utils.html import mark_safe
from shortuuid.django_fields import ShortUUIDField
# from django.conf import settings
import uuid
import random
import string
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

########### import settings ##############


STATUS_CHOICES = (
    ("available", "Available"),
    ("booked", "Booked"),
    ("delivered", "Delivered"),
    ("detached", "Detached"),
    ("processing", "Processing"),
)

STATUS = (
    ("draft", "Draft"),
    ("published", "Published"),
    ("in_review", "In Review"),
    ("disabled", "Disabled"),
    ("rejected", "Rejected"),
)

RATINGS = (
    ("1", '★'),
    ("2", '★★'),
    ("3", '★★★'),
    ("4", '★★★★'),
    ("5", '★★★★★'),
)





def user_directory_path(instance, filename):
     return 'user_{0}/{1}'.format(instance.user.id, filename)

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def profile(self):
        profile = Profile.objects.get(user=self)
        return profile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    bio = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media", default="default.jpg")
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

def generate_cid():
    return 'cat'+ str(uuid.uuid4()).replace('-', '')[:8] + ''.join(random.choices(string.ascii_letters + string.digits, k=4))
Category_id = generate_cid()
class Category(models.Model):

    cid = ShortUUIDField(unique=True, default=Category_id, max_length=30)

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category', default='default.jpg')

    class Meta:
        verbose_name_plural = 'Categories'

    def category_image(self):
        return mark_safe('<img src="%s" width="100" height="100" />' % self.image.url)

    def __str__(self):
        return self.title
############# fucntion to get  vendor id  ######################
def generate_vid():
    return 'ven' + str(uuid.uuid4()).replace('-', '')[:8] + ''.join(random.choices(string.ascii_letters + string.digits, k=4))
vendor_id = generate_vid()
# print(vendor_id)
class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tags'

############# define Tags class model ######################
# class Tag(TagBase):
#     class Meta:
#         verbose_name = _("Tag")
#         verbose_name_plural = _("Tags")
#         app_label = 'taggit'
# class ItemBase(models.Model):

#     def __str__(self):
#         return gettext("%(object)s tagged with %(tag)s") % {
#             "object": self.object, 'tag': self.tag
#             }
#     class Meta:
#         abstract = True
#         # app_label = 'taggit'
#         # unique_together = ('content_type', 'object_id', 'tag')
#         # verbose_name = _("Tagged Item")
#         # verbose_name_plural = _("Tagged Items")
# @classmethod
# def tag_model(cls):
#         field=cls._meta.get_field("tag")
#         return field.remote_field.model

class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, default=vendor_id, max_length=30)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=100)
    date_created= models.DateTimeField(auto_now_add=True, null=True, blank=True)
    contact = models.CharField(max_length=100, default='+ 91 (123) 456')
    address = models.CharField(max_length=100, default='456 Main street, Rajkok, Rjt 36003, India.')
    bio = models.CharField(max_length=100)
    image = models.ImageField(upload_to='user_directory_path', default='default.jpg')
    cover_image = models.ImageField(upload_to='user_directory_path', default='default.jpg')
    verified = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    # description = models.TextField(null=True, blank=True)
    description = RichTextUploadingField (null=True, blank=True)
    chat_rest_time = models.CharField(max_length=100) 
    authenticate_rating = models.CharField(max_length=100, default='100')
    days_return = models.CharField(max_length=100, default='100') 
    warrant_period = models.CharField(max_length=100, default='100') 
    shipping_on_time = models.CharField(max_length=100, default='100')
    

    class Meta:
        verbose_name_plural = 'Vendors'

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.image.url)

    def __str__(self):
        return self.full_name
     
############# fucntion to get  item id  ######################
def generate_iid():
    return 'it' + str(uuid.uuid4()).replace('-', '')[:8] + ''.join(random.choices(string.ascii_letters + string.digits, k=4))
item_id = generate_iid()   
    
class Item(models.Model):
    
    iid= ShortUUIDField(unique=True, default=item_id, max_length=30)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, related_name='item')
    title = models.CharField(max_length=100)
    # description = models.TextField(default='This is a description of the Item  goes here .')
    description =  RichTextUploadingField(default='This is a description of the Item  goes here .')
    image = models.ImageField(upload_to='user_directory_path', default='default.jpg')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,related_name='category')
    price = models.DecimalField(max_digits=15, decimal_places=2, default=1.99)
    old_price = models.DecimalField(max_digits=15, decimal_places=2, default=2.99)
    # specifications = models.TextField(null=True, blank=True)
    specifications = RichTextUploadingField(null=True, blank=True)
    length = models.CharField(max_length=50, blank=True, null=True, default="4.00m") 
    width = models.CharField(max_length=50,  blank=True, null=True, default="3.00m")
    height = models.CharField(max_length=50,  blank=True, null=True, default="0.60m")
    weight = models.CharField( max_length=50, blank=True, null=True, default="5.60kg")
    tags = TaggableManager(blank=True)
    available_quantity = models.IntegerField(default=1)
    stock_count= models.CharField( max_length=50,default=200)
    min_rental_duration = models.CharField(max_length=50, default="1 day" )
    max_rental_duration = models.CharField(max_length=50, default="30 Days " )
    item_status = models.CharField(choices=STATUS, max_length=20, default='in_review')
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Items'

    def item_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.image.url)

    def __str__(self):
        return self.title

    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price

class ItemImages(models.Model):
    images = models.ImageField(upload_to='item_images', default='item.jpg')
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, related_name='i_images')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Item Images'

class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=1.99)
    paid_status = models.BooleanField(default=False)
    booked_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(auto_now_add=True)
    item_status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='processing')

    class Meta:
        verbose_name_plural = 'Rentals'

    def __str__(self):
        return self.title

class RentalItem(models.Model):
    booking = models.ForeignKey(Rental, on_delete=models.CASCADE)
    item_status = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=1.99)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=1.99)

    class Meta:
        verbose_name_plural = 'RentalItems'

    def Rentalitem_images(self):
        return mark_safe('<img src="/media/" width="50" height="50" />' % self.image)

class ItemReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, related_name='reviews')
    review = models.TextField()
    rating = models.IntegerField(choices=RATINGS, default=2)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Item Reviews'

    def __str__(self):
        return self.item.title

    def get_rating(self):
        return self.rating

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Wishlists'

    def __str__(self):
        return self.item.title

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.address
