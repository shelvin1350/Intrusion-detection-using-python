"""CyberSpy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Cyberapp import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', views.Home, name='Home'),
     path('', views.Home, name='Home'),
    path('Registration', views.Registration, name='Registration'),
    path('login/', views.login, name='login'),
    
    path('feedback', views.feedback, name='feedback'),
    path('file_sharing/', views.file_sharing, name='file_sharing'),
    path('filecontent', views.filecontent, name='filecontent'),
    path('threatlist', views.threatlist, name='threatlist'),
    path('attack_defining', views.attack_defining, name='attack_defining'),
    path('user_home', views.user_home, name='user_home'),
    path('No_threats/', views.No_threats, name='No_threats'),
    
    path('view_profile', views.view_profile, name='view_profile'),
    path('add_data', views.add_data, name='add_data'),
    path('attacks', views.attacks, name='attacks'),
    path('notifications', views.notifications, name='notifications'),
    path('rat', views.rat, name='rat'),
    path('Attacks', views.Attacks, name='Attacks'),
    
    path('user_edit_profile', views.user_edit_profile, name='user_edit_profile'),
    path('edit_fname', views.edit_fname, name='edit_fname'),
    path('edit_sname', views.edit_sname, name='edit_sname'),
    path('edit_email', views.edit_email, name='edit_email'),
    path('edit_pswd', views.edit_pswd, name='edit_pswd'),
    path('new_profile', views.new_profile, name='new_profile'),
    path('threat_findings', views.threat_findings, name='threat_findings'),
    path('Inbox_empty', views.Inbox_empty, name='Inbox_empty'),
    
    
    path('file_inbox', views.file_inbox, name='file_inbox'),
    path('inbox_view', views.inbox_view, name='inbox_view'),
    path('msg_reply', views.msg_reply, name='msg_reply'),
    path('Cyber_attacks', views.Cyber_attacks, name='Cyber_attacks'),
    path('reply_view',views.Reply_view,name='reply_view'),

    path('ddos', views.ddos, name='ddos'),
    path('man_in_the_middle', views.man_in_the_middle, name='man_in_the_middle'),
    path('phishing', views.phishing, name='phishing'),
    path('keylogger', views.keylogger, name='keylogger'),
    path('exploit', views.exploit, name='exploit'),
    path('adware', views.adware, name='adware'),
    path('infected_usb', views.infected_usb, name='infected_usb'),
    path('ransomeware', views.ransomeware, name='ransomeware'),
    path('sms_sender', views.sms_sender, name='sms_sender'),
    
    path('logout', views.logout, name='logout'),
    
    path('head_tail', views.head_tail, name='head_tail'),
    path('head2_tail2', views.head2_tail2, name='head2_tail2'),

    
   
]+staticfiles_urlpatterns() + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
