from rest_framework import serializers
from .models import Phone

class Phoneserializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['phonenumber',]