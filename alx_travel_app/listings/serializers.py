# serializers.py
from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class InitPaymentSerializer(serializers.Serializer):
    booking_id   = serializers.IntegerField()
    email        = serializers.EmailField()
    callback_url = serializers.URLField()

class VerifyPaymentSerializer(serializers.Serializer):
    reference    = serializers.CharField()
