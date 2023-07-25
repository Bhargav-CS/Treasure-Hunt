"""mywebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.landing_page, name='landing_page'),
    path('round1/', views.round1, name='round1'),  # We'll create this view later
    path('round1_success/', views.round1_success, name='round1_success'),  # Ensure this URL pattern is already defined
    # Add the URL for Round 2
    path('round2/', views.round2, name='round2'),
    
    path('round3/', views.round3, name='round3'),
    path('submit_solution/', views.submit_solution, name='submit_solution'),
    
    
]

