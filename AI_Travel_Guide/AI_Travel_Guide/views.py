from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Trip, Preferences, MyUser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.models import User
from rest_framework import status
import json

@api_view(['POST'])
def register_view(request):
    pass
    print('reg called')
    try:
        data = request.data
        print(type(data))
        print(data)
        print('register called')
        if 'email' not in data:
            data['email'] = data['auth0_user_id']
        user = MyUser.objects.create(
            auth0_user_id=data['auth0_user_id'],
            email=data['email'],
            email_verified=data['email_verified'],
            phone_number=data['phone_number'],
            profile_picture=data['profile_picture'],
            username=data['name'],
        )
        
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        print(f"Error: {e}")  # Log the exception for debugging
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def recommend_view_input(request):
    try:
        data = request.data
        print(data)

        # Convert data types
        data['distance'] = int(data['distance'])
        data['budget'] = int(data['budget'])
        data['duration'] = int(data['duration'])

        # Extract user data from the request
        user_data = data.get('user')
        if not user_data:
            return Response({"error": "User data is required"}, status=400)

        # Retrieve or create the MyUser instance
        user, created = MyUser.objects.get_or_create(
            auth0_user_id=user_data['sub'],  # Use unique identifier from Auth0
            defaults={
                'email': user_data.get('email','sub'),
                'name': user_data.get('name', 'Anonymous'),
                'profile_picture': user_data.get('picture', ''),
                'email_verified': user_data.get('email_verified', False),
            }
        )

        # Store preferences in the database
        preferences, created = Preferences.objects.get_or_create(
            user=user,
            defaults={
                'max_distance': data['distance'],
                'budget': data['budget'],
                'duration': data['duration'],
            }
        )

        # If Preferences already exist, update them
        if not created:
            preferences.max_distance = data['distance']
            preferences.budget = data['budget']
            preferences.duration = data['duration']
            preferences.save()

        print('Preferences saved successfully!')

        # Mock response - replace with actual API calls (e.g., Google Maps, Weather)
        recommendations = {
            "destinations": [
                {"name": "Goa", "distance": 500, "cost": 10000, "duration": 3},
                {"name": "Manali", "distance": 600, "cost": 15000, "duration": 5},
            ],
            "packing_checklist": ["Sunscreen", "Comfortable Shoes", "Raincoat"],
        }

        return Response(recommendations)
    except Exception as e:
        print("Error:", str(e))
        return Response({"error": str(e)}, status=500)

