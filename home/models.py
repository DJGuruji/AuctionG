from django.db import models
from django.contrib.auth.models import User
class AuctionListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_bid = models.DecimalField(max_digits=10, decimal_places=2)
    reserve_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2)
    auction_end = models.DateTimeField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    def __str__(self):
      return self.title
    

class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
      return self.bidder.username
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
      return self.name

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add fields for user profile details

class Feedback(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback_given')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback_received')
    feedback_text = models.TextField()
    rating = models.PositiveSmallIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Create your models here.
