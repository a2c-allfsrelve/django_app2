
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('training/', include('db_training.urls')), #db_trainingで使われるURL
]
