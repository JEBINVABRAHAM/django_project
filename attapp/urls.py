from django.views.generic import TemplateView
from django.urls import path
from .import views
urlpatterns= [
      path('',TemplateView.as_view(template_name='index.html'),name='index'),
      path('login/',TemplateView.as_view(template_name='login.html'),name='login'),
      path('adminhome/',TemplateView.as_view(template_name='adminhome.html'),name='adminhome'),
      path('submit',views.display,name='submits'),
      path('submitss',views.fsignup,name='sssubmit'),
      path('studentsignup/',TemplateView.as_view(template_name='studentsignup.html'),name='studentsignup'),
      path('facultysignup/',TemplateView.as_view(template_name='facultysignup.html'),name='facultysignup'),
      path('studentdetails/',TemplateView.as_view(template_name='studentdetails.html'),name='studentdetails'),
      path('facultydetails/',TemplateView.as_view(template_name='facultydetails.html'),name='facultydetails'),
      path('timetable/',TemplateView.as_view(template_name='timetable.html'),name='timetable'),
      path('facultyattendance/',TemplateView.as_view(template_name='facultyattendance.html'),name='facultyattendance'),
      path('studentattendance/',TemplateView.as_view(template_name='studentattendance.html'),name='studentattendance'),
      path('facultyhome/',TemplateView.as_view(template_name='facultyhome.html'),name='facultyhome'),
      path('studenthome/',TemplateView.as_view(template_name='studenthome.html'),name='studenthome'),
      path('facdetails',views.viewfacpro,name='facultydetails'),
      path('studetails',views.viewstupro,name='studentdetails'),
      path('alldetails',views.viewallfac,name='allfaculty'),
      path('allstudetails',views.viewallstu,name='allstudent'),
      path('facultystudetails/',TemplateView.as_view(template_name='fstuddetails.html'),name='fstuddetails'),
      path('facstuddetails',views.viewfacstud,name='fstuddetails'),
      path('facultymarks/',TemplateView.as_view(template_name='facmarks.html'),name='facmarks'),
      path('facultymark',views.viewfmarks,name='facmarks'),
      path('addmarks',views.fmarks,name='sssubmits'),
      path('allstudentmarks/',TemplateView.as_view(template_name='allstudmarks.html'),name='allstudmarks'),
      path('allstudntmark/',views.viewfacmarks,name='allstudmarks'),
      path('studntmark',views. viewstudmarks,name='allstudmarks'),
      path('facstudentatt/',TemplateView.as_view(template_name='facstudattendance.html'),name='facstudattendance'),
      path('attendance',views.stuattendance,name='addattendance'),
      path('adminatt',views.adminattendance,name='studentattendance'),
      path('adminmarks/',TemplateView.as_view(template_name='admarks.html'),name='admarks'),
      path('admark',views.adminmarks,name='admarks'),
      path('stumark/',TemplateView.as_view(template_name='studmarks.html'),name='studmarks'),
      path('studentm',views.stumarks,name='studmarks'),
      path('studentatt/',TemplateView.as_view(template_name='stuattendance.html'),name='stuattendance'),
      path('stuatt',views.stuattend,name='stuattendance'),
      path('studleav/',TemplateView.as_view(template_name='studentleave.html'),name='studentleave'),
      path('stdleave',views.stuleave,name='stleave'),
      path('leavemanag/',TemplateView.as_view(template_name='adminleave.html'),name='adminleave'),
      path('sleave',views.studleave,name='adminleave'),
      path('leaveapprove',views.approvestud,name='approve'),
      path('leavestatus/',TemplateView.as_view(template_name='studentleavestatus.html'),name='studentleavestatus'),
      path('sstatus',views.approvedleave,name='studentleavestatus'),
      path('fleave',TemplateView.as_view(template_name='facultyleave.html'),name='facultyleave'),
      path('facleave',views.facleave,name='facultyl'),
      path('fccleave',TemplateView.as_view(template_name='adminfacleave.html'),name='adminfacleave'),
      path('faccl',views.approvefac,name='adminfacleave'),
      path('leaveapp',views.approvedfac,name='approved'),
      path('facleaves/',TemplateView.as_view(template_name='facultyleavestatus.html'),name='facultyleavestatus'),

      path('stuedd/',TemplateView.as_view(template_name='studentedit.html'),name='studentedit'),
      path('ffleaves',views.approvedstatusfac,name='facultyleavestatus'),
      path('fdits',TemplateView.as_view(template_name='facultyedit.html'),name='facultyedit'),
      path('editf',views.editdetails,name='fedits'),
      path('editf',views.editdetails,name='facultyedit'),
      path('submits',views.authentication,name='ssubmit'),
      path('sssu',views.facdetailsedit,name='faced'),
      path('editss',views.editstud,name='studedits'),
      path('editssss',views.editstud,name='studentedit'),
      path('editstu',views.studetailsedit,name='stued'),
      path('sout',views.logout_view,name='signout'),
      path('facstudatten/',TemplateView.as_view(template_name='facultystudattendance.html'),name='facultystudattendance'),
      path('facultyatt',views.facstudentattendance,name='facultystudattendance'),



]