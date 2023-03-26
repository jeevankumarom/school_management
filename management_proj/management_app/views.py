from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from .models import *
from rest_framework import status
from .serializers import *
import json
from rest_framework.decorators import api_view

from .utilities import *

import secrets
import string


class index(APIView):

    def get(self,request):
        return Response("School Management")
    


class register_school(APIView):
    

    def post(self,request):
        """
    
        post method will register a new school, and if it is true, it will return "Successfully register."
        Otherwise, if an error exception is encountered, it will return "some error"; otherwise, it will return "already exists." 
        
        """
        try:
            if school.objects.filter(name=self.request.data['name']).exists() == False:
                serializers=school_serializers(data=self.request.data)
                serializers.is_valid(raise_exception=True)
                serializers.save()
                return Response(status=status.HTTP_200_OK,data="Successfully register")
            else:
                return Response(status=status.HTTP_200_OK,data=f"{self.request.data['name']}  Already exists" )
        except Exception as e:
            return Response(status=status.HTTP_307_TEMPORARY_REDIRECT,data=str(e))
        
    def get(self,request):
        """

            If there are no parameters in the URL, it will return all the data.
            If some parameters are passed, it will filter. If data exists, it will return.
        """
        try:
            if len(request.GET) == 0:
                query=school.objects.all()
                serializer=school_serializers(instance=query,many=True)
                return Response(status=status.HTTP_200_OK,data=serializer.data)
            else:
                
                json_=json.dumps(request.GET)
                json_1=json.loads(json_)
                query=school.objects.filter(**json_1)
                serializer=school_serializers(instance=query,many=True)
                return Response(status=status.HTTP_200_OK,data=serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_202_ACCEPTED,data=str(e))
        

class register_classes(APIView):
    
    def post(self,request):

        """
            If the school is already registered, 
            upload it for each class and save it with the registered school ID. 
        """

        try:
            temp_dict=self.request.data.copy()

            school_id=get_school_id(temp_dict['school'])

            temp_dict['school']=school_id
            if classes.objects.filter(name=temp_dict['name']).exists() == False:
                serializers=class_serializers(data=temp_dict)
                serializers.is_valid(raise_exception=True)
                serializers.save()
                return Response(status=status.HTTP_200_OK,data="Successfully registred")
            else:
                return Response(status=status.HTTP_200_OK,data="Already Exists")

        except Exception as e:
            return Response(status=status.HTTP_307_TEMPORARY_REDIRECT,data=str(e))
        

    def get(self,request):
        """
        
            If we want to know how many classes each school has, using In Postman, we should search "school=SPVM."

        
        """
        try:
            if len(request.GET) == 0:
                query=classes.objects.all()
                serializer=class_serializers(instance=query,many=True)
                return Response(status=status.HTTP_200_OK,data=serializer.data)
            else:
                
                json_=json.dumps(request.GET)
                json_1=json.loads(json_)




                try:
                    school_id=get_school_id(json_1['school'])
                    json_1['school']=school_id

                except:
                    pass

                query=classes.objects.filter(**json_1)

                serializer=class_serializers(instance=query,many=True)
                return Response(status=status.HTTP_200_OK,data=serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_202_ACCEPTED,data=str(e))
        

    

class register_section(APIView):
    """
        If the school is already registered,
        Upload it for multiple sections a class ID it has mentioned by foreignkey. 
        """
    def post(self,request):
        try:
            temp_dict=self.request.data.copy()

            school_id=get_school_id(temp_dict['school'])

            temp_dict['school']=school_id
            if section.objects.filter(name=temp_dict['name']).exists() == False:
                serializers=section_serializers(data=temp_dict)
                serializers.is_valid(raise_exception=True)
                serializers.save()
                return Response(status=status.HTTP_200_OK,data="Successfully registred")
            else:
                return Response(status=status.HTTP_200_OK,data="Already Exists")

        except Exception as e:
            return Response(status=status.HTTP_307_TEMPORARY_REDIRECT,data=str(e))
        

    def get(self,request):
        """
        If we want to know how many sections each school has, using In Postman, we should search "school=SPVM."

        
        """
        try:
            if len(request.GET) == 0:
                query=section.objects.all()
                serializer=section_serializers(instance=query,many=True)
                return Response(status=status.HTTP_200_OK,data=serializer.data)
            else:
                
                json_=json.dumps(request.GET)
                json_1=json.loads(json_)
                try:
                    school_id=get_school_id(json_1['school'])
                    json_1['school']=school_id

                except:
                    pass

                query=section.objects.filter(**json_1)

                serializer=section_serializers(instance=query,many=True)
                return Response(status=status.HTTP_200_OK,data=serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_202_ACCEPTED,data=str(e))
        

class register_subjects(APIView):
    """
        If the school is already registered,
        Upload it for multiple subjects with a class ID it has mentioned by foreignkey.

    """
    def post(self,request):
        try:
            temp_dict=self.request.data.copy()

            school_id=get_school_id(temp_dict['school'])

            temp_dict['school']=school_id
            if subject.objects.filter(name=temp_dict['name']).exists() == False:
                serializers=subject_serializers(data=temp_dict)
                serializers.is_valid(raise_exception=True)
                serializers.save()
                return Response(status=status.HTTP_200_OK,data="Successfully registred")
            else:
                return Response(status=status.HTTP_200_OK,data="Already Exists")

        except Exception as e:
            return Response(status=status.HTTP_307_TEMPORARY_REDIRECT,data=str(e))
        

    def get(self,request):
        """
        If we want to know how many subjects for each school has, using In Postman, we should search like "school=SPVM."
        
        """
        try:
            if len(request.GET) == 0:
                query=subject.objects.all()
                serializer=subject_serializers(instance=query,many=True)
                return Response(status=status.HTTP_200_OK,data=serializer.data)
            else:
                
                json_=json.dumps(request.GET)
                json_1=json.loads(json_)
                try:
                    school_id=get_school_id(json_1['school'])
                    json_1['school']=school_id

                except:
                    pass

                query=subject.objects.filter(**json_1)

                serializer=subject_serializers(instance=query,many=True)
                return Response(status=status.HTTP_200_OK,data=serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_202_ACCEPTED,data=str(e))
        


class register_student(APIView):

    """
        If the student has registered with sections like "A," "B," "C," and classes like "10," "11," "12,"
        It will pass the utils function and get the generated ID for classes and sections pass into students model.
        If the students details has been uploaded, it will automatically upload login credentials for students.
    """

    def post(self,request):

        tempdict=self.request.data.copy()

        section_id=get_sction_id(tempdict['section'])

        class_id=get_classes_id(tempdict['classes'])
        
        school_id=get_school_id(tempdict['school'])

        student_id=creating_student_and_staff_id(tempdict['school'],'students')
       
        alphabet = string.ascii_letters + string.digits
        
        tempdict['section'] = section_id
        tempdict['classes'] = class_id
        tempdict['school'] = school_id
        tempdict['student_id']=student_id


        try:

            
            serializers=student_serializers(data=tempdict)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            
            
            user_password=self.request.data['school'].lower().replace(" ","")
            tempdict['student']=serializers.data['student_id']

            tempdict['user_name'] = f"{self.request.data['school']}_{tempdict['name']}"

            password = ''.join(secrets.choice(alphabet) for i in range(4))
            
            tempdict['password'] = f"{user_password}{tempdict['name'].lower()}_{password}"
            
            loginserializer=login_serializers(data=tempdict)

            loginserializer.is_valid(raise_exception=True)

            loginserializer.save()

            

            return Response(status=status.HTTP_200_OK,data={"student_id":serializers.data['student_id'],"user_name":tempdict['user_name'],"password":tempdict['password'],"status":"student login credentials created"})

        except Exception as e:

            return Response(status=status.HTTP_307_TEMPORARY_REDIRECT,data={"status":str(e)})

    def get(self,request):

        try:
            if len(request.GET) == 0:
                query=students.objects.all()
                serializer=student_serializers(instance=query,many=True)
                return Response(status=status.HTTP_200_OK,data=serializer.data)
            else:
                
                json_=json.dumps(request.GET)
                json_1=json.loads(json_)
                try:
                    school_id=get_school_id(json_1['school'])
                    json_1['school']=school_id

                except:
                    pass

                query=students.objects.filter(**json_1)

                serializer=student_serializers(instance=query,many=True)
                return Response(status=status.HTTP_200_OK,data=serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_202_ACCEPTED,data=str(e))
        

class register_staff(APIView):
    """
        If the staff has registered with sections like ["A," "B," "C,"] and classes like ["10," "11," "12,"]
        It will not pass the utils function and get the generated ID because staff having multiple classes and section
        so it will store as an array for class and sections.
        If the staff has been uploaded, it will automatically upload login credentials for staff.
    """
    def post(self,request):

        tempdict=self.request.data.copy()

        school_id=get_school_id(tempdict['school'])

        student_id=creating_student_and_staff_id(tempdict['school'],'staffs')
        
        alphabet = string.ascii_letters + string.digits

        tempdict['school'] = school_id
        tempdict['staff_id']=student_id

        try:

            
            serializers=staff_serializers(data=tempdict)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            
            
            user_password=self.request.data['school'].lower().replace(" ","")
            tempdict['staff']=serializers.data['staff_id']

            tempdict['user_name'] = f"{self.request.data['school']}_{tempdict['name']}"

            password = ''.join(secrets.choice(alphabet) for i in range(4))
            
            tempdict['password'] = f"{user_password}{tempdict['name'].lower()}_{password}"
            
            loginserializer=login_serializers(data=tempdict)

            loginserializer.is_valid(raise_exception=True)

            loginserializer.save()

            return Response(status=status.HTTP_200_OK,data={"user_name":tempdict['user_name'],"password":tempdict['password'],"status":"staff login credentials created"})

        except Exception as e:

            return Response(status=status.HTTP_307_TEMPORARY_REDIRECT,data={"status":str(e)})

    def get(self,request):

        try:
            if len(request.GET) == 0:
                query=staffs.objects.all()
                serializer=staff_serializers(instance=query,many=True)
                return Response(status=status.HTTP_200_OK,data=serializer.data)
            else:
                
                json_=json.dumps(request.GET)
                json_1=json.loads(json_)
                try:
                    school_id=get_school_id(json_1['school'])
                    json_1['school']=school_id

                except:
                    pass

                query=staffs.objects.filter(**json_1)

                serializer=staff_serializers(instance=query,many=True)
                return Response(status=status.HTTP_200_OK,data=serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_202_ACCEPTED,data=str(e))
        


class login_check(APIView):
    
    """
    we should pass a key with login_condition = student or staff,
    which will check whether the user_name and password match or not.
    """
    def post(self,request):

        try:
            if request.data['login_condition'] == 'student':

                if login_info.objects.filter(user_name=request.data['user_name']).exists():
                    if login_info.objects.filter(user_name=request.data['user_name'],password=request.data['password'],staff_id=None).exists():
                        return Response(f"{request.data['login_condition']} login successfully")
                    else:
                        return Response(status=status.HTTP_200_OK,data="password does not matched")
                else:
                    return Response(status=status.HTTP_200_OK,data="Username does not matched")
            else:
                if login_info.objects.filter(user_name=request.data['user_name'],student_id=None).exists():
                    if login_info.objects.filter(user_name=request.data['user_name'],password=request.data['password'],student_id=None).exists():
                        return Response(status=status.HTTP_200_OK,data={"status":f"{request.data['login_condition']} login successfully"})
                    else:
                        return Response(status=status.HTTP_200_OK,data="password does not matched")
                else:
                    return Response(status=status.HTTP_200_OK,data="Username does not matched")
        
        except Exception as e:
            return Response(status=status.HTTP_202_ACCEPTED,data=str(e))
class Rank_system(APIView):

    

    def post(self,request):
        """
        Place the students' grades in the marks table under the registered school name.        
        
        """
        try:
            tempdict=request.data.copy()
            school_id=get_school_id(tempdict['school'])
            tempdict['school']=school_id
            print(tempdict['student'])
            if students.objects.filter(student_id=tempdict['student']).exists():
                serializers=rank_serializers(data=tempdict)
                serializers.is_valid(raise_exception=True)
                serializers.save()
                return Response(status=status.HTTP_200_OK,data="mark submitted successfully")
            else:
                return Response(status=status.HTTP_202_ACCEPTED,data="Check student id")
        except Exception as e:
            return Response(status=status.HTTP_202_ACCEPTED,data=str(e))

    def get(self,request):
        """
        The student rank system mentions classes by name; for example, 
        if you filter out 10th grade, it will show responses from top marks.4

        """

        student = students.objects.select_related('rank_set').filter(classes__name=self.request.GET['class']).values('student_id','name', 'classes__name','section__name' ,'marks__mark').order_by('-marks__mark')
        ranked_marks=[]
        rank=0
        for i, student in enumerate(student):
            rank+=1
            student["Rank"] = rank
            ranked_marks.append(student)
        return Response(ranked_marks)
    


"""
create Students and Staff login from in-built model
 
"""
from django.contrib.auth import authenticate,login


class staffRegisterview(APIView):
    def post(self,request):
        tempdict=self.request.data.copy()

        sec=get_sction_id(tempdict['sec'])

        clas=get_classes_id(tempdict['cls'])
        
        school_id=get_school_id(tempdict['school'])

        staff_id=creating_student_and_staff_id(tempdict['school'],'staff')

        tempdict['cls']=clas
        tempdict['sec']=sec
        # tempdict['staff_id']=staff_id
        tempdict['is_staff']=True
        tempdict['school']=school_id
        print(tempdict)
        serializer = StaffSerializer(data=tempdict)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StaffLoginView(APIView):
    def get(self, request):
        print("CALLED")
        email = request.GET['email']
        password = request.GET['password']
        print(email,password)
        user = authenticate(email=email, password=password)
        print(user)
        # if user and user.is_staff:
        login(request, user)
        serializer = StaffSerializer(user,many=True)
        return Response(serializer.data)
        # else:
        #     return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
