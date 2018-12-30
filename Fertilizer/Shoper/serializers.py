from django.shortcuts import render, get_object_or_404
from rest_framework import serializers
from django.http import JsonResponse
from .models import Student

def students_detail(request, pk):
    su = get_object_or_404(Student, pk=pk)
    data = {"results": { "name": su.name, "lastName": su.lastName, "email": su.email }}
    return JsonResponse(data)

class StudentSerializer(serializers.Serializer):
    """class Meta:
        model = Student
        fields = '__all__' 
        """
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length=250)
    lastName = serializers.CharField(max_length=250)
    email = serializers.CharField(max_length=300)

    def create(self , validated_data):
        return Student.objects.create(**validated_data)
