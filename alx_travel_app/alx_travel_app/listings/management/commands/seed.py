from django.core.management.base import BaseCommand
from alx_travel_app.alx_travel_app.listings.models import Listing


class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **options):
        sample_data = [
            {'title': 'Cozy Beach House', 'description': 'Steps from the ocean.', 'price': 150.00, 'location': 'Miami, FL'},
            {'title': 'Mountain Cabin Retreat', 'description': 'Secluded and serene.', 'price': 200.00, 'location': 'Aspen, CO'},
            {'title': 'Urban Loft', 'description': 'In the heart of the city.', 'price': 120.00, 'location': 'New York, NY'},
            {'title': 'Countryside B&B', 'description': 'Charming farmhouse.', 'price': 80.00, 'location': 'Nashville, TN'},
            {'title': 'Desert Glamping', 'description': 'Luxury under the stars.', 'price': 180.00, 'location': 'Sedona, AZ'},
        ]

        for data in sample_data:
            listing, created = Listing.objects.get_or_create(
                title=data['title'],
                defaults={
                    'description': data['description'],
                    'price': data['price'],
                    'location': data['location'],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Listing already exists: {listing.title}"))
