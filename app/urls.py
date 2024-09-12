from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('student/<str:dept>',views.student,name="student"),
    path('instructor/<str:dept>',views.instructor,name="instructor"),
    path('instrument/<str:dept>',views.instrument,name="instrument"),
    path('add_student',views.add_student,name="add_student"),
    path('add_instructor',views.add_instructor,name="add_instructor"),
    path('add_instrument',views.add_instrument,name="add_instrument"),
    path('add_department',views.add_department,name="add_department"),
    path('user_login',views.user_login,name="user_login"),
    path('signup',views.signup,name="signup"),
    path('user_logout',views.user_logout,name="user_logout"),
    path('delete_instrument/<str:pk>',views.delete_instrument,name="delete_instrument"),
    path('delete_instructor/<str:pk>',views.delete_instructor,name="delete_instructor"),
    path('delete_student/<str:pk>',views.delete_student,name="delete_student"),
    path('delete_department/<str:pk>',views.delete_department,name="delete_department"),
    path('delete_notice/<str:pk>',views.delete_notice,name="delete_notice"),
    path('search',views.search,name="search"),
    path('add_notice',views.add_notice,name="add_notice"),
    path('notice',views.notice,name="notice"),
]