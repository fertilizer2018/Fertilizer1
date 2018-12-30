
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from . import serializers
#from . apiviews import StudentList
#from . apiviews import studentAll
from . import apiviews


urlpatterns = [
    path('a/', views.shoper_login, name='ShoperForm'),
    path('signup/', views.signup, name='signup'),
    path('signup1/', views.signup1, name='signup1'),
    #path("student/<int:pk>/", serializers.students_detail, name="students_detail"),
    #path("student1/", StudentList.as_view(), name="StudentSerializer"),
    path("student2/", apiviews.studentAll),

]

urlpatterns = format_suffix_patterns(urlpatterns)
