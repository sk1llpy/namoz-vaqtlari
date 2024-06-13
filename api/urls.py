from django.urls import path
from rest_framework import permissions

from . import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path


schema_view = get_schema_view(
   openapi.Info(
      title="Namoz Vaqtlari API",
      default_version='v1',
      description="API documentation for your project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="abdullohnugmonovone222@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('users/', views.UsersListApiView.as_view()),
    path('users/get/', views.UserGetApiView.as_view()),
    path('users/create/', views.CreateUserApiView.as_view()),
    path('users/update/region/', views.UpdateUserRegionApiView.as_view()),
    path('users/update/notification/', views.UpdateUserNotificationApiView.as_view()),
    path('users/filter/region/', views.FilterUsersApiView.as_view()),

    path('prayer-times/day/', views.PrayerTimesDailyApiView.as_view()),
    path('prayer-times/week/', views.PrayerTimesWeeklyApiView.as_view()),

    path('tasbih/update/', views.UpdateTasbihApiView.as_view()),
    path('tasbih-mode/update/', views.UpdateTasbihModeApiView.as_view()),

    # Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]