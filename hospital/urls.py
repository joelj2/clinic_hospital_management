from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    # path("base/",views.home,name="home"),
    path("",views.base,name="base"),
    path("tempadmin/",views.admin,name="tempadmin"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path("user/",views.user,name="user"),
    path("userreg/",views.user_registration,name="user_reg"),
    path("login/",views.user_login,name="login"),
    path("department/",views.department_list,name="department"),
    path("update_dep/<int:id>",views.update_department,name="update_dep"),
    path("delete_dep/<int:id>",views.delete_department,name="delete_dep"),
    path("create_doctor/",views.create_doctor,name="create_doctor"),
    path("doctor_list/",views.doctor_list,name="doctor_list"),
    path("update_doc/<int:id>",views.update_doctor,name="update_doc"),
    path("appointment_form/",views.appointment_form,name="appointment"),
    path("appointment_form_list/",views.appointment_form_list,name="appointment_list"),
    path("manage_appointment/",views.manage_appointment,name="manage_appointment"),
    path("appointment_approve/<int:id>",views.appointment_approve,name="appointment_approve"),
    path("appointment_reject/<int:id>",views.appointment_reject,name="appointment_reject"),
    path('addslot/',views.add_slot,name="addslot"),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="hospital/reset_password.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="hospital/reset_password_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="hospital/new_password.html"),name="password_reset_confirm"),       
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="hospital/password_reset_complete.html"),name="password_reset_complete"),

    
]