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


print('callllled')
@api_view(['POST'])
def recommend_view(request):
    data = request.data
    user_id = 12342
    distance = data.get('distance')
    budget = data.get('budget')
    duration = data.get('duration')
    print(distance)
    print(budget)
    print(duration)
    
    # Store in the database
    preferences = Preferences.objects.create(
        # destination="",  # Placeholder if no specific destination is provided
        user_id = user_id,
        max_distance=distance,
        budget=budget,
        duration=duration,
    )
    print('ALLLLLLLLL GOOOOODD')
    # Mock response - replace with actual API calls (e.g., Google Maps, Weather)
    recommendations = {
        "destinations": [
            {"name": "Goa", "distance": 500, "cost": 10000, "duration": 3},
            {"name": "Manali", "distance": 600, "cost": 15000, "duration": 5},
        ],
        "packing_checklist": ["Sunscreen", "Comfortable Shoes", "Raincoat"],
    }

    return Response(recommendations)
