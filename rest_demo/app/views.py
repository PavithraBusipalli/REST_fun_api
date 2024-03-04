from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.response import Response 
# Create your views here.
@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def StudentJsonData(request):
    SMO = Student.objects.all()
    SSO = FuncSerializer(SMO,many=True)
    JSD = SSO.data 
    return Response(JSD)
