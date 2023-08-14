from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .utils import scrape_licence_number_plate
import requests
from .utils import scrape_licence_number_plate
# Create your views here.
from .serializers import RegisteredVehicleSerializer
from .models import RegisteredVehicle



class IndexAPIView(APIView):
    permission_classes = [AllowAny]
    
    
    def get(self, request):
        return Response({'message': 'Server active'})

    def post(self, request):
        try:
            file_image = request.FILES['file']
            # Set the URL of the target server
            url = 'https://app.platerecognizer.com/alpr-demo'
            proxy_url = 'http://192.168.8.102:8800/'
            # Set the CSRF token
            csrf_token = 'lRI6NWO8zH1S2qVmTbd73B9eghN3kL36utVCAxMkgkA1Ij6vTAsidvgiJWLCgExJ'  # Replace with the actual CSRF token

            # Set the headers including the CSRF token
            headers = {
                'X-CSRFToken': csrf_token,
                'Origin': 'https://app.platerecognizer.com'
            }

            files = {'upload': file_image}
            # Send the POST request with the form data and file
            response = requests.post(url, files=files, headers=headers)
            # Process the response
            if response.status_code == 200:
                try:
                    data = response.json()
                    return Response({"data": data})
                except ValueError:
                    # Response is not in JSON format
                    content = response.content
                    plate_number = scrape_licence_number_plate(content)
                    # Querying for vehicle
                    vehicle = RegisteredVehicle.objects.filter(plate_number=plate_number)
                    if vehicle.exists():
                        data = RegisteredVehicleSerializer(vehicle).data
                        return Response({"data": data})
                    else:
                        return Response({"data": "Vehicle not registered!"}, 403)

            return Response({"data": "Unauthorized"}, 401)
        except Exception as e:
            return Response({"data": e}, 403)






