from django.urls import path
import  electronics.views as views


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'buyers', views.ProviderCRUD, basename='byers')
urlpatterns = router.urls

