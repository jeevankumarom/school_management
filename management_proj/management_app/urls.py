from django.urls import path
from .views import *

urlpatterns=[

    path('',index.as_view()),
    path('schools/',register_school.as_view()),
    path('classes/',register_classes.as_view()),
    path('section/',register_section.as_view()),
    path('subjects/',register_subjects.as_view()),
    path('students/',register_student.as_view()),
    path('staffs/',register_staff.as_view()),
    path('login_check/',login_check.as_view()),
    path('Rank_system/',Rank_system.as_view()),
    path('StaffLoginView/',StaffLoginView.as_view()),
    path('staffRegisterview/',staffRegisterview.as_view())
    # path('creating_student_id/<str:school>',creating_student_id)

]