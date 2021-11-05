from django.shortcuts import render
from .models import Booking, User,Adviser
from rest_framework.views import Response,APIView,status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
import datetime

# Create your views here.

class BookingView(APIView):
    def get(self,request,user_id=None,adviser_id=None):
        booking=Booking.objects.all()
        details=[]
        for data in booking:
            result={
                'Adviser Name':data.adviser.adviser_name,
                'Adviser Profile Pic':data.adviser.adviser_photo_url,
                'Adviser Id':data.adviser.adviser_id,
                'Booking time': data.booking_time,
                'Booking id':data.booking_id

            }
            details.append(result)
        return Response(data=details)

    def post(self,request,user_id=None,adviser_id=None):
        time=request.data['Booking Time']
        time=time.split(',')
        a=[int(i) for i in time]
        booking_time=datetime.datetime(a[0],a[1],a[2],a[3],a[4],a[5])
        adviser=Adviser.objects.get(adviser_id=adviser_id)
        already,booking=Booking.objects.get_or_create(adviser=adviser,booking_time=booking_time)
        if booking:
            return Response(status=status.HTTP_200_OK)

        return Response(data={'Adviser Name':already.adviser.adviser_name,
        'Booking Time':already.booking_time})


class AdviserPost(APIView):
    def post(self,request):
        try:
            name=request.data['Adviser Name']
            photo_url=request.data['Adviser Photo URL']

            adviser,newadviser=Adviser.objects.get_or_create(adviser_name=name,adviser_photo_url=photo_url)

            if newadviser:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(f"Adviser is already Available,('id':{adviser.adviser_id},'name':{adviser.adviser_name})",status=status.HTTP_302_FOUND)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class AdviserView(APIView):
    # permission_classes=[IsAuthenticated]

    def get(self,request,user_id=None):
        advisers=Adviser.objects.all()
        adviser_details=[]
        for adviser in advisers:
            result={
                "Advisor Name":adviser.adviser_name,
                "Advisor Profile Pic":adviser.adviser_photo_url,
                "Advisor Id":adviser.adviser_id
            }
            adviser_details.append(result)

        return Response(data=adviser_details,status=status.HTTP_200_OK)

class Login(APIView):

    def post(self,request):
        try:
            email=request.data['email']
            password=request.data['password']
            user=User.objects.get(email=email)
            if user and (user.password==password):
                token=RefreshToken.for_user(user)
                return Response(data={"userid":user.id,
                "token":{"refresh":str(token),
                        "access":str(token.access_token)}})
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class Register(APIView):

    def post(self,request):
        name=request.data['name']
        email=request.data['email']
        password=request.data['password']
        user,createuser=User.objects.get_or_create(user_name=name,email=email,password=password)
        if createuser:
            newuser=User.objects.last()
            token=RefreshToken.for_user(newuser)
            return Response(data={"userid":newuser.id,
            "token":{"refresh":str(token),
                    "access":str(token.access_token)}},status=status.HTTP_200_OK)
            
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
           

