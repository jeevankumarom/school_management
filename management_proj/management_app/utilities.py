from .models import *

from .serializers import *

import random

"""
Common Functions

"""

def get_school_id(name):
    
    try:
        query=school.objects.filter(name=name).values('school_id')
        print(query)
        return query[0]['school_id']
    except Exception as e:

        return str(e)
    

def get_sction_id(name):
    try:
        query=section.objects.filter(name=name).values('section_id')
        return query[0]['section_id']
    except Exception as e:
        return e

    
def get_classes_id(name):
    try:
        query=classes.objects.filter(name=int(name)).values('class_id')
        # print()
        return query[0]['class_id']
    except Exception as e:
        return e

def creating_student_and_staff_id(name,condition):

    try:
        if condition == 'students':
            # school=request.GET['school']
            # sch=school.lower().replace(" ","")

            school_name = name
            std_id = school_name + str(random.randint(1000, 9999))

            find_id=True

            while find_id==True:
                if students.objects.filter(student_id=std_id).exists() == False:
                    find_id=False
                else:
                    std_id = school_name + str(random.randint(1000, 9999))


            return std_id
        else:

            
            # school=request.GET['school']
            # sch=school.lower().replace(" ","")

            school_name = name
            stf_id = school_name + str(random.randint(1000, 9999))

            find_id=True

            while find_id==True:
                if staffs.objects.filter(staff_id=stf_id).exists() == False:
                    find_id=False
                else:
                    stf_id = school_name + str(random.randint(1000, 9999))


            return stf_id

    
    except Exception as e:
        print(str(e))
        pass
