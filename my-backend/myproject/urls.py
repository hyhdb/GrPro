from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mychat/', include('mychat.urls')),  # mychat 앱의 URL을 'mychat/'로 포함
    path('', include('myapp.urls')),  # 다른 앱들은 'myapp/' URL을 포함
]
