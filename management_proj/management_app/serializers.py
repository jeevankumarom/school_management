from rest_framework import serializers
from .models import *


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