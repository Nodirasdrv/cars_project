from django.urls import path, include
from rest_framework.routers import DefaultRouter
from category_cars import views

router = DefaultRouter()
router.register('', views.CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),

    # path('', views.CreateCategory.as_view()),
    # path('list/', views.ListCategory.as_view()),
    # path('detail/<int:pk>', views.UpdateCategory.as_view()),
]
