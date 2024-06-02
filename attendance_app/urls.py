from django.urls import path
from .import views

urlpatterns=[
      path('admin_home',views.admin_home,name='admin_home'),
      path('employee_home',views.employee_home,name='employee_home'),
      path('',views.user_login,name='login'),
      path('logout',views.user_logout,name='logout'),
      path('create_user',views.create_user,name='create_user'),
      path('departments',views.departments,name='departments'),
      path('employee_profile_update',views.employee_profile_update_admin,name='employee_profile_update'),
      path('user_profile',views.profile,name='user_profile'),
      path('profiles_admin',views.profiles_admin,name='profiles_admin'),
      path('leave_employee',views.leave_employee,name='leave_employee'),
      path('leave_requests_admin',views.leave_requests_admin,name='leave_requests_admin'),
      path('view_leave_request_admin/<int:i>',views.view_leave_request,name='view_leave_request_admin'),
      path('reject',views.reject_leave,name='reject'),
      path('approve',views.approve_leave,name='approve'),
      path('attendance_admin',views.attendance_admin,name='attendance_admin'),
      path('date_filter',views.date_filter,name='date_filter'),
      path('filter_attendance_employee',views.filter_attendance_employee,name='filter_attendance_employee'),
      path('employee_attendance',views.employee_attendance,name='employee_attendance')
]