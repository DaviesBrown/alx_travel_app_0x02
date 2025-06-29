from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    ListingViewSet, BookingViewSet, InitializePaymentView, VerifyPaymentView
)

router = DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = router.urls + [
    path('payments/init/', InitializePaymentView.as_view(), name='payment-init'),
    path('payments/verify/', VerifyPaymentView.as_view(), name='payment-verify'),
]
