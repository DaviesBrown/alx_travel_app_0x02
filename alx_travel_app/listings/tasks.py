from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_payment_confirmation(email, booking_id):
    send_mail(
        subject='Booking Confirmed',
        message=f'Your booking #{booking_id} is confirmed!',
        from_email='no-reply@yourdomain.com',
        recipient_list=[email],
    )
