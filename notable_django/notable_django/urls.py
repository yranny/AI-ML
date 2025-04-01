from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapi.views import ItemViewSet

# 创建一个路由器实例
router = DefaultRouter()
router.register(r'items', ItemViewSet)  # 注册视图集到路由器

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # 包含 API 路由
]

