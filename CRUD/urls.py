from django.conf.urls import url  
from django.contrib import admin  
from CRUD_FBVs import views  
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
   
app_name = 'CRUD_FBVs'  
   
urlpatterns = [  
    url('admin/', admin.site.urls),  
    url(r'^$', views.movies_list, name='movies_list'),
    url(r'^new$', views.movies_create, name='movies_new'),

     
 ]  
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
