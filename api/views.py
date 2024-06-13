import requests
from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from bot.data.regions import REGIONS


class UsersListApiView(APIView):
    def get(self, request):
        users = models.Users.objects.all()  # Fetch all users from the database
        user_data = [{'id': user.id, 'user_id': user.user_id, 'notification': user.notification} for user in users]  # Extract user_id from each user object

        return Response(
            data={
                'message': 'List of users retrieved successfully',
                'data': user_data
            },
            status=status.HTTP_200_OK
        )


class FilterUsersApiView(APIView):
    def post(self, request):
        users = models.Users.objects.filter(region=request.data.get('region'))  # Fetch all users from the database
        user_data = [{'id': user.user_id, 'notification': user.notification, 'region': user.region} for user in users]  # Extract user_id from each user object

        return Response(
            data={
                'message': 'List of users retrieved successfully',
                'data': user_data
            },
            status=status.HTTP_200_OK
        )



class UserGetApiView(APIView):
    def post(self, request):
        try:
            user = models.Users.objects.get(user_id=request.data.get("user_id"))

            return Response(
                data={
                    'user_id': user.user_id,
                    'tasbih': user.tasbih_counter,
                    'mode': user.tasbih_mode,
                    'region': user.region,
                    'notification': user.notification
                }
            )
        except user.DoesNotExist:
            return Response(
                data={
                    'status': 400,
                    'message': 'User not found',
                    'data': {'user_id': request.data.get("user_id")}
                }
            )


class CreateUserApiView(APIView):
    def post(self, request):
        data = request.data
        user_id = data.get("user_id")  # Use .get() to avoid KeyError

        try:
            user = models.Users.objects.get(user_id=user_id)

            return Response(
                data={
                    'message': 'User already exists',
                    'data': data
                },
                status=status.HTTP_200_OK
            )
        except models.Users.DoesNotExist:
            user = models.Users.objects.create(user_id=user_id).save()

            return Response(
                data={
                    'message': 'User created successfully',
                    'data': data
                },
                status=status.HTTP_201_CREATED
            )
        

class UpdateUserRegionApiView(APIView):
    def post(self, request):
        data = request.data
        user_id = data.get("user_id")
        region = data.get("region")

        user = models.Users.objects.get(user_id=user_id)
        user.region = region
        user.save()

        return Response(
            data={
                'message': 'User update successfully',
                'data': data
            },
            status=status.HTTP_200_OK
        )
    

class UpdateUserNotificationApiView(APIView):
    def post(self, request):
        data = request.data
        user_id = data.get("user_id")
        notification = data.get("notification")

        user = models.Users.objects.get(user_id=user_id)
        user.notification = notification
        user.save()

        return Response(
            data={
                'message': 'User update successfully',
                'data': data
            },
            status=status.HTTP_200_OK
        )


class PrayerTimesDailyApiView(APIView):
    def post(self, request):
        region = request.data.get('region')

        def get_prayer_times(region):
            url = f'https://islomapi.uz/api/present/day?region={region}'
            response = requests.get(url)

            return response.json()
        
        if region in REGIONS:
            data = get_prayer_times(region=region)
            
            return Response(
                data={
                    'message': f'Prayer time of {region} retrieved successfully',
                    'data': data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data={
                    'message': f'Prayer time of {region} not found',
                    'data': data
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        

class PrayerTimesWeeklyApiView(APIView):
    def post(self, request):
        region = request.data.get('region')

        def get_prayer_times(region):
            url = f'https://islomapi.uz/api/present/week?region={region}'
            response = requests.get(url)

            return response.json()
        
        if region in REGIONS:
            data = get_prayer_times(region=region)
            
            return Response(
                data={
                    'message': f'Prayer time of {region} retrieved successfully',
                    'data': data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data={
                    'message': f'Prayer time of {region} not found',
                    'data': data
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class UpdateTasbihApiView(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        count = int(request.data.get("count"))

        try:
            user_update = models.Users.objects.get(user_id=user_id)
            user_update.tasbih_counter = count
            user_update.save()

            return Response(data={
                'message': "Tasbih updated succesfully",
                'data': {
                    'user_id': user_id,
                    'tasbih': count
                }
            }, status=status.HTTP_200_OK)
        except user_update.DoesNotExist:
            return Response(
                data={
                    'status': 400,
                    'message': 'User not found',
                    'data': {'user_id': request.data.get("user_id")}
                }
            )
    

class UpdateTasbihModeApiView(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        count = int(request.data.get("mode"))

        try:
            user_update = models.Users.objects.get(user_id=user_id)
            user_update.tasbih_mode = count
            user_update.save()

            return Response(data={
                'message': "Tasbih mode updated succesfully",
                'data': {
                    'user_id': user_id,
                    'mode': count
                }
            }, status=status.HTTP_200_OK)
        except user_update.DoesNotExist:
            return Response(
                data={
                    'status': 400,
                    'message': 'User not found',
                    'data': {'user_id': request.data.get("user_id")}
                }
            )
