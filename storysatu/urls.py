"""storysatu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    # story 1 dan 4
    path('', include('cerita1.urls')),

    # story 5
    path('story5/', include('cerita5.urls')),

    # story 6
    path('story6/', include('cerita6.urls')),

    # story 7
    path('story7/', include('cerita7.urls')),

    # story 8
    path('story8/', include('cerita8.urls')),

    # story 9
    path('story9/', include('cerita9.urls')),

    # api
    path('snip_api/', include('snippets.urls')),

]
