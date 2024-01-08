from django.contrib import admin
from django.urls import include, path
from movieDB.views import MovieListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movieDB/', include('movieDB.urls')),
]
