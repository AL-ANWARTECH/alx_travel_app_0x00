from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
from django.utils import timezone
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        
        # Create superuser if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write('Created superuser: admin')
        
        # Create sample users
        users = []
        user_data = [
            {'username': 'john_doe', 'email': 'john@example.com'},
            {'username': 'jane_smith', 'email': 'jane@example.com'},
            {'username': 'bob_wilson', 'email': 'bob@example.com'},
            {'username': 'alice_brown', 'email': 'alice@example.com'},
        ]
        
        for data in user_data:
            user, created = User.objects.get_or_create(
                username=data['username'],
                defaults={'email': data['email']}
            )
            if created:
                user.set_password('password123')
                user.save()
                self.stdout.write(f'Created user: {user.username}')
            users.append(user)
        
        # Create sample listings
        listings_data = [
            {
                'title': 'Beautiful Beach House',
                'description': 'Stunning beachfront property with amazing ocean views',
                'property_type': 'house',
                'price_per_night': 250.00,
                'location': 'Miami, FL',
                'max_guests': 6,
                'bedrooms': 3,
                'bathrooms': 2,
                'amenities': 'WiFi, Pool, Kitchen, Parking'
            },
            {
                'title': 'Cozy Downtown Apartment',
                'description': 'Modern apartment in the heart of downtown',
                'property_type': 'apartment',
                'price_per_night': 120.00,
                'location': 'New York, NY',
                'max_guests': 2,
                'bedrooms': 1,
                'bathrooms': 1,
                'amenities': 'WiFi, Gym, Elevator'
            },
            {
                'title': 'Luxury Mountain Villa',
                'description': 'Spacious villa with mountain views and private hot tub',
                'property_type': 'villa',
                'price_per_night': 400.00,
                'location': 'Aspen, CO',
                'max_guests': 8,
                'bedrooms': 4,
                'bathrooms': 3,
                'amenities': 'WiFi, Hot Tub, Fireplace, Garage'
            },
            {
                'title': 'Rustic Cabin Retreat',
                'description': 'Peaceful cabin surrounded by nature',
                'property_type': 'cabin',
                'price_per_night': 180.00,
                'location': 'Lake Tahoe, CA',
                'max_guests': 4,
                'bedrooms': 2,
                'bathrooms': 1,
                'amenities': 'WiFi, Fireplace, BBQ, Hiking Trails'
            },
            {
                'title': 'City Center Hotel Suite',
                'description': 'Luxury hotel suite with premium amenities',
                'property_type': 'hotel',
                'price_per_night': 300.00,
                'location': 'Los Angeles, CA',
                'max_guests': 2,
                'bedrooms': 1,
                'bathrooms': 1,
                'amenities': 'WiFi, Room Service, Pool, Spa, Gym'
            }
        ]
        
        listings = []
        for listing_data in listings_data:
            listing, created = Listing.objects.get_or_create(
                title=listing_data['title'],
                defaults=listing_data
            )
            if created:
                self.stdout.write(f'Created listing: {listing.title}')
            listings.append(listing)
        
        # Create sample bookings
        booking_data = [
            {
                'listing': listings[0],
                'user': users[0],
                'check_in_date': timezone.now().date() + timedelta(days=7),
                'check_out_date': timezone.now().date() + timedelta(days=10),
                'guests': 2,
                'status': 'confirmed'
            },
            {
                'listing': listings[1],
                'user': users[1],
                'check_in_date': timezone.now().date() + timedelta(days=14),
                'check_out_date': timezone.now().date() + timedelta(days=16),
                'guests': 2,
                'status': 'pending'
            },
            {
                'listing': listings[2],
                'user': users[2],
                'check_in_date': timezone.now().date() + timedelta(days=21),
                'check_out_date': timezone.now().date() + timedelta(days=25),
                'guests': 4,
                'status': 'confirmed'
            }
        ]
        
        for booking_info in booking_data:
            # Calculate total price
            nights = (booking_info['check_out_date'] - booking_info['check_in_date']).days
            total_price = nights * booking_info['listing'].price_per_night
            
            booking, created = Booking.objects.get_or_create(
                listing=booking_info['listing'],
                user=booking_info['user'],
                check_in_date=booking_info['check_in_date'],
                check_out_date=booking_info['check_out_date'],
                defaults={
                    'guests': booking_info['guests'],
                    'status': booking_info['status'],
                    'total_price': total_price
                }
            )
            if created:
                self.stdout.write(f'Created booking: {booking}')
        
        # Create sample reviews
        reviews_data = [
            {
                'listing': listings[0],
                'user': users[1],
                'rating': 5,
                'comment': 'Amazing place! The view was breathtaking.'
            },
            {
                'listing': listings[0],
                'user': users[2],
                'rating': 4,
                'comment': 'Great location and comfortable stay.'
            },
            {
                'listing': listings[1],
                'user': users[0],
                'rating': 3,
                'comment': 'Good value for money, but a bit noisy.'
            }
        ]
        
        for review_data in reviews_data:
            review, created = Review.objects.get_or_create(
                listing=review_data['listing'],
                user=review_data['user'],
                defaults={
                    'rating': review_data['rating'],
                    'comment': review_data['comment']
                }
            )
            if created:
                self.stdout.write(f'Created review: {review}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully seeded the database!')
        )