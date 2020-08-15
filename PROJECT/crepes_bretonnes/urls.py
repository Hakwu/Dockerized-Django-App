from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'crepes_bretonnes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', views.registerPage, name='register'),
    url(r'^admin/', include(admin.site.urls)),
    url('blog/', include('blog.urls')),
    url('login/', views.loginPage, name='login'),
    url('profil', views.profilPage, name='profil'),
]
