# ALX Travel App - Milestone 1

## Overview
This milestone focuses on defining database models, creating serializers for API data representation, and implementing a management command to seed the database with sample data.

## Features Implemented
- **Database Models**: Listing, Booking, and Review models with proper relationships
- **Serializers**: REST API serializers for Listing and Booking models
- **Database Seeder**: Management command to populate the database with sample data

## Models

### Listing
- Title, description, property type, price per night
- Location, guest capacity, bedrooms, bathrooms
- Amenities and availability status

### Booking
- Foreign key relationship with Listing and User
- Check-in/check-out dates, guest count
- Total price calculation and booking status

### Review
- Foreign key relationship with Listing and User
- Rating (1-5 stars) and comment
- Unique constraint to prevent duplicate reviews

## Setup Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt