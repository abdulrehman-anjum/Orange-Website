from django.urls import path
from home import views 

urlpatterns = [
	path('', views.index, name='home'),
	path('register', views.register, name='register'),
	path('show_employees', views.show_employees, name='show_employees'),
	path('employee/<int:id>/delete', views.delete_employee, name='delete_employee'),
	path('employee/<int:id>/update', views.update_employee, name='update_employee'),
]