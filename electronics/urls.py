import  electronics.views as views


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'providers', views.ProviderCRUD, basename='providers')
urlpatterns = router.urls

