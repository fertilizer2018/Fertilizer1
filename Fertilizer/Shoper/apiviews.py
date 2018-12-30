from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Student
from .serializers import StudentSerializer



@api_view(['POST'])
def studentAll(request):
    #if request.mehod == 'POST':
    print("request.data : ",request.data)
    stud = StudentSerializer(data= request.data)
    if stud.is_valid():
       stud.save()
       return Response(stud.data , status=status.HTTP_201_CREATED)
    return Response(stud.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentList(APIView):
    def get(self, request):
        polls = Student.objects.all()[:20]
        data = StudentSerializer(polls, many=True).data
        return Response(data)




