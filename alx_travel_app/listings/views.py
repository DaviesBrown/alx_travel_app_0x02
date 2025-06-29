# views.py
from rest_framework import viewsets, status
from .models import Listing, Booking, Payment
from .serializers import ListingSerializer, BookingSerializer, InitPaymentSerializer, VerifyPaymentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .paystack import PaystackClient
from django.shortcuts import get_object_or_404

class InitializePaymentView(APIView):
    def post(self, request):
        serializer = InitPaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data      = serializer.validated_data
        booking   = get_object_or_404(Booking, pk=data['booking_id'])

        # Kick off Paystack transaction
        amount_kobo = int(booking.total_amount * 100)
        res = PaystackClient.initialize(
            email=data['email'],
            amount=amount_kobo,
            callback_url=data['callback_url']
        )

        # Persist Payment record
        ref = res['data']['reference']
        Payment.objects.create(
            booking   = booking,
            reference = ref,
            amount    = amount_kobo,
            status    = 'pending'
        )

        return Response(res, status=status.HTTP_200_OK)


class VerifyPaymentView(APIView):
    def post(self, request):
        serializer = VerifyPaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ref       = serializer.validated_data['reference']
        res       = PaystackClient.verify(ref)

        payment   = get_object_or_404(Payment, reference=ref)
        status_str = res['data']['status']
        payment.status = status_str
        payment.transaction = res['data'].get('id')
        payment.save()
        from .tasks import send_payment_confirmation
        send_payment_confirmation.delay(payment.booking.user.email, payment.booking.id)


        return Response({
            'reference': ref,
            'status': status_str,
            'authorization': res['data'].get('authorization'),
        }, status=status.HTTP_200_OK)

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

