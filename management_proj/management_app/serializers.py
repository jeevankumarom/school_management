from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class school_serializers(serializers.ModelSerializer):
    class Meta:
        model=school
        fields='__all__'

class class_serializers(serializers.ModelSerializer):
    class Meta:
        model=classes
        fields='__all__'


class section_serializers(serializers.ModelSerializer):
    class Meta:
        model=section
        fields='__all__'

class subject_serializers(serializers.ModelSerializer):
    class Meta:
        model=subject
        fields='__all__'

class student_serializers(serializers.ModelSerializer):
    class Meta:
        model=students
        fields='__all__'

class staff_serializers(serializers.ModelSerializer):
    class Meta:
        model=staffs
        fields='__all__'

class login_serializers(serializers.ModelSerializer):
    class Meta:
        model=login_info
        fields='__all__'

class rank_serializers(serializers.ModelSerializer):
    
    class Meta:
        model=marks
        fields='__all__'




# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['id', 'email', 'first_name', 'last_name', 'roll_number']

# class StaffSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Staff_register_login
#         fields = ['id', 'email', 'first_name', 'last_name','sec','cls','school','password']    
    
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
        
#         user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

#         return user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
