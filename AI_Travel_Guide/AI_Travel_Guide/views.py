from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Trip, Preferences, MyUser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.models import User
from rest_framework import status
import json
from django.core.cache import cache  
import requests

OLLAMA_URL = "http://localhost:11500/api/generate"

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


@api_view(['POST'])
def recommend_view_input(request):
    try:
        data = request.data
        print(data)

        # Convert data types
        data['distance'] = int(data['distance'])
        data['budget'] = int(data['budget'])
        data['duration'] = int(data['duration'])

        # Save the data in cache (can be replaced with a database if needed)
        cache.set('recommendation_data', data, timeout=3600)  # 1-hour timeout
        # Extract user data from the request
        user_data = data.get('user')
        if not user_data:
            return Response({"error": "User data is required"}, status=400)

        # Retrieve or create the MyUser instance
        user, created = MyUser.objects.get_or_create(
            auth0_user_id=user_data['sub'],  # Use unique identifier from Auth0
            defaults={
                'email': user_data.get('email','sub'),
                'username': user_data.get('name', 'Anonymous'),
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

        from backend.api.foursquare import recommend_api
    
        latitude, longitude, radius, budget = data['latitude'], data['longitude'], data['distance'], data['budget']
        response = recommend_api(latitude, longitude, radius, budget)

        destinations = []
        for places in response['results']:
            destinations.append({
                "name":places['name'],
                "address": places['location']['formatted_address'],
                "categories": [category['id'] for category in places['categories']],
                "fsq_id": places['fsq_id'],
            })
        
        # print(destinations)
        response = {
            "destinations": destinations,
            "packing_checklist": ["Clothes", "Snacks", "Camera", "Power Bank"]
        }
        return Response(response, status=200)
    except Exception as e:
        print("Error:", str(e))
        return Response({"error": str(e)}, status=500)
    
@api_view(['POST'])
def chatbot(request):
    # Use request.data instead of request.json
    user_prompt = request.data.get("prompt", "")
    model_name = "travelbuddy"  # Custom model name

    # Sending request to Ollama
    data = {"model": model_name, "prompt": user_prompt, "stream" : False}

    response = requests.post(OLLAMA_URL, json=data)
    print(response.text)
    try:
        response_json = response.json()  # Convert to a dictionary
        print("Extracted response:", response_json.get("response", "No response found"))  # Extract chatbot reply

    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
    # Check if response is successful
    if response.status_code == 200:
        return Response(response_json)  # Return JSON response
    else:
        return Response({"error": "Failed to fetch response from Ollama"}, status=500)
    

# @api_view(['POST'])
# def chatbot(request):
#     """
#     Handles chat requests with history using Django session.
#     """
#     try:
#         user_prompt = request.data.get("prompt", "")
#         print(user_prompt)
#         model_name = "travelbuddy"  # Custom model name

#         if not user_prompt:
#             return Response({"error": "Message cannot be empty."}, status=400)

#         # Retrieve chat history from session or initialize it
#         chat_history = request.session.get("chat_history", [])
#         print(chat_history)
#         # Append user message to chat history
#         chat_history.append({"role": "user", "content": user_prompt})
#         print(chat_history)
#         # Construct payload correctly
#         data = {
#             "model": model_name,
#             "messages": chat_history,  # ✅ Use messages instead of prompt
#             "stream": False
#         }
#         print(data)
#         # Sending request to Ollama
#         response = requests.post(OLLAMA_URL, json=data)
#         print(response.text)
#         if response.status_code == 200:
#             response_data = response.json()

#             # Append assistant response to chat history
#             assistant_message = response_data["message"]["content"]
#             chat_history.append({"role": "assistant", "content": assistant_message})

#             # Save updated chat history to session
#             request.session["chat_history"] = chat_history

#             return Response(response_data)
#         else:
#             return Response({"error": "Ollama API request failed", "details": response.text}, status=500)

#     except Exception as e:
#         return Response({"error": str(e)}, status=500)

# @api_view(['POST'])
# def clear_chat_history(request):
#     """
#     Clears chat history for the user.
#     """
#     request.session["chat_history"] = []
#     return Response({"message": "Chat history cleared."})