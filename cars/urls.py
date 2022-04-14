from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.CarViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('', views.CreateCarAPIView.as_view()),
    # path('update/<int:pk>/', views.UpdateCarAPIView.as_view()),
    # path('detail/<int:pk>/', views.DeleteDetailCarAPIView.as_view()),
]
