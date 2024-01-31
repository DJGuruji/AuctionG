from django.contrib import admin
from .models import AuctionListing, Bid, Category, Message, UserProfile, Feedback

@admin.register(AuctionListing)
class AuctionListingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AuctionListing._meta.fields]

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bid._meta.fields]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Message._meta.fields]

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserProfile._meta.fields]

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Feedback._meta.fields]
