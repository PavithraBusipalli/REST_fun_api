from rest_framework import serializers
from .models import *
class FuncSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['sid','sname']
        