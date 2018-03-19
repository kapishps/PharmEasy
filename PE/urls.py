"""PE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth.decorators import login_required

from django.contrib.auth import views
from PEapp.views import PrescriptionDetailView, MedicalRecordDetailView,home, signup,create_approval, approve_approval
from PEapp.admin import LoginForm, UserCreationForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', auth_views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('signup/', signup, name='signup'),
    path('prescription/<int:pk>', login_required(PrescriptionDetailView.as_view()), name='prescription-detail'),
    path('medicalrecord/<int:id>', login_required(MedicalRecordDetailView.as_view()), name='medicalrecord-detail'),
    path('create_approval/', create_approval, name='create_approval'),
    path('approve_approval/', approve_approval, name='approve_approval'),

]
