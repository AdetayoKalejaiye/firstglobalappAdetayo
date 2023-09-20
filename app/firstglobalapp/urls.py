"""firstglobalapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from forms import views as formViews
from documentation import views as docViews
from gamefield import views as gameViews
from chat import urls as chatUrls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', formViews.signUp, name="signUp"),
    path('signIn/', formViews.signIn, name="signIn"),
    path('home/', formViews.home, name="home"),
    path('docs/', docViews.documents, name="docs"),
    path('game/', gameViews.game, name='game'),
    path('chat/', include('chat.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
