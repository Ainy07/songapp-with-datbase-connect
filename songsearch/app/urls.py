from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.base),
    path("login/",views.login),
    path("signup/",views.signup),
    path('registration/',views.registration),
    path('login_data/',views.login_form),
    path('songs/',views.songs),
    # path('search/',views.search),
    # path('api/top/tracks/',views. get_top_tracks , name="get_top_tracks"),
    # path('tracks/',views.track_list , name="track_list"), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
