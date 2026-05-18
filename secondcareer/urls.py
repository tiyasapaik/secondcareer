from django.contrib import admin
from django.urls import path,include
from secondcareer import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   path('admin/', admin.site.urls),
   path('',views.index,name='home'),
   path('contact',views.contact,name='contact'),
   path('account',views.account,name='account'),
   path('organizer',views.organizer,name='organizer'),
   path('register_user',views.register_user,name='register_user'),
   path('register_organizer',views.register_organizer,name='register_organizer'),
   path('login_public',views.login_public,name='login_public'),
   path('login',views.login_page,name='login'),
   path('login_company',views.login_company,name='login_company'),
   path('login_page1',views.login_page1,name='login_page1')
 
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
)
urlpatterns+=staticfiles_urlpatterns()