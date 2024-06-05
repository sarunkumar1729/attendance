from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from .models import department,employee_profile,leave_requests,attendance
from datetime import date
# Create your views here.

def admin_home(request):
      return render(request,'admin/admin_home.html')

def employee_home(request):
      return render(request,'employee/employee_home.html')

def user_login(request):
      if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                  login(request,user)
                  if user.is_staff:
                        return redirect('admin_home')
                  else:
                        return redirect('employee_home')
            else:
                  print("login failed")
                  return render(request,'login.html')
      else:
            return render(request,'login.html')

def user_logout(request):
      logout(request)
      return redirect('login')

def create_user(request):
      if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            user = User.objects.create(
                  username = username,
                  password = make_password(password),
                  first_name = first_name,
                  last_name = last_name,
                  email = email
            )
            user.save()
            print("successfully registered")
            return render(request,'admin/create_employee.html')
      else:
            return render(request,'admin/create_employee.html')

def departments(request):
      if request.method=='POST':
            dep = request.POST['department']
            new_department = department(title=dep)
            new_department.save()
            all_departments = department.objects.all()
            return render(request,'admin/departments.html',{'departments':all_departments})
      else:
            all_departments = department.objects.all()
            return render(request,'admin/departments.html',{'departments':all_departments})
      
def employee_profile_update_admin(request):
      if request.method=='POST':
            user=request.POST['user']
            user=User.objects.get(username=user)
            department_id=request.POST['department']
            emp_department=department.objects.get(id=department_id)
            employee_id=request.POST['emp_id']
            photo=request.FILES.get('profile_photo')
            gender=request.POST['gender']
            age=request.POST['age']
            address=request.POST['address']
            phone=request.POST['phone']
            email=request.POST['email']
            joining_date=request.POST['joining_date']
            starting_salary=request.POST['starting_salary']
            current_salary=request.POST['current_salary']
            if not employee_profile.objects.filter(user=user):
                  new_profile=employee_profile(
                        user=user,
                        employee_id=employee_id,
                        profile_photo=photo,
                        gender=gender,
                        age=age,
                        address=address,
                        phone=phone,
                        email=email,
                        department=emp_department,
                        joining_date=joining_date,
                        starting_salary=starting_salary,
                        current_salary=current_salary
                  )
                  new_profile.save()
            # else:
            #       new_profile=employee_profile.objects.get(user=user)
            #       new_profile.employee_id=employee_id
            #       new_profile.profile_photo=photo,
            #       new_profile.gender=gender,
            #       new_profile.age=age,
            #       new_profile.address=address,
            #       new_profile.phone=phone,
            #       new_profile.email=email,
            #       new_profile.department=emp_department,
            #       new_profile.joining_date=joining_date,
            #       new_profile.starting_salary=starting_salary,
            #       new_profile.current_salary=current_salary
            #       new_profile.save()
            return render(request,'admin/employee_profile.html')
      else:
            users=User.objects.all()
            departments=department.objects.all()
            return render(request,'admin/employee_profile.html',{'users':users,'departments':departments})
      
# display profile by user
def profile(request):
      current_user=request.user
      profile=employee_profile.objects.get(user=current_user)
      print(current_user)
      print(profile)
      return render(request,'employee/profile.html',{'profile':profile})

def profiles_admin(request):
      employees=employee_profile.objects.all()
      return render(request,'admin/profiles_admin.html',{"employees":employees})

def leave_employee(request):
      current_user=request.user
      if request.method=='POST':
            date=request.POST['date']
            message=request.POST['message']
            new_leave_request=leave_requests(user=current_user,date=date,message=message)
            new_leave_request.save()
            leave_request=leave_requests.objects.filter(user=current_user)
            return render(request,'employee/leave_details.html',{'leave_requests':leave_request})      
      else:
            leave_request=leave_requests.objects.filter(user=current_user)
            return render(request,'employee/leave_details.html',{'leave_requests':leave_request})
      
def leave_requests_admin(request):
            requests=leave_requests.objects.all()
            return render(request,'admin/leave_requests.html',{'requests':requests})

def view_leave_request(request,i):
      global leave_request
      leave_request=leave_requests.objects.get(id=i)
      profile=employee_profile.objects.get(user=leave_request.user)
      return render(request,'admin/leave_request.html',{'leave_request':leave_request,'profile':profile})

def reject_leave(request):
      leave_request.status='rejected'
      leave_request.save()
      requests=leave_requests.objects.all()
      return render(request,'admin/leave_requests.html',{'requests':requests})

def approve_leave(request):
      leave_request.status='approved'
      leave_request.save()
      requests=leave_requests.objects.all()
      return render(request,'admin/leave_requests.html',{'requests':requests})

def attendance_admin(request):
      if request.method=='POST':
            emp=request.POST['employee']
            status=request.POST['status']
            emp=employee_profile.objects.get(id=emp)
            if not attendance.objects.filter(user=emp,status=status):
                  new_attendance=attendance(user=emp,status=status)
                  new_attendance.save()
            print('attendance added')
            employees=employee_profile.objects.all()
            today=date.today()
            todays_attendance=attendance.objects.filter(date=today)
            # todays_attendance=attendance.objects.all()
            employees=employee_profile.objects.all()
            return render(request,'admin/attendance.html',{'employees':employees,'attendance':todays_attendance})      
      else:
            today=date.today()
            todays_attendance=attendance.objects.filter(date=today)
            # todays_attendance=attendance.objects.all()
            employees=employee_profile.objects.all()
            return render(request,'admin/attendance.html',{'employees':employees,'attendance':todays_attendance})

def date_filter(request):
      get_date=request.POST['date']
      filtered_attendance=attendance.objects.filter(date=get_date)
      print(filtered_attendance)
      today=date.today()
      todays_attendance=attendance.objects.filter(date=today)
            # todays_attendance=attendance.objects.all()
      employees=employee_profile.objects.all()
      return render(
            request,'admin/attendance.html',
            {'employees':employees,'attendance':todays_attendance,'filtered_attendance':filtered_attendance}
            )

def filter_attendance_employee(request):
      emp_id=request.POST['id']
      try:
            emp=employee_profile.objects.get(id=emp_id)
            filtered_attendance=attendance.objects.filter(user=emp)
      except:
            filtered_attendance=None
      employees=employee_profile.objects.all()
      today=date.today()
      todays_attendance=attendance.objects.filter(date=today)
      return render(
            request,'admin/attendance.html',
            {'employees':employees,'attendance':todays_attendance,'filtered_attendance':filtered_attendance}
            )

def employee_attendance(request):
      user=request.user
      emp=employee_profile.objects.get(user=user)
      your_attendance=attendance.objects.filter(user=emp)
      return render(request,'employee/attendance.html',{'attendance':your_attendance})

def delete_profile(request,i):
      profile=employee_profile.objects.get(id=i)
      profile.delete()
      return redirect('profiles_admin')