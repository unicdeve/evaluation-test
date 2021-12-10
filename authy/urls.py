from rest_framework.routers import DefaultRouter

from .views import LoginViewSet, LogoutViewSet, UserViewSet

router = DefaultRouter()
router.register("login", LoginViewSet, base_name="login")
router.register("logout", LogoutViewSet, base_name="logout")
router.register("", UserViewSet, base_name="users")


urlpatterns = router.urls
