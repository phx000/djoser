from django.contrib.auth import get_user_model
from rest_framework.routers import DefaultRouter

from djoser import views

router = DefaultRouter(trailing_slash=False)
router.register("users", views.UserViewSet)

User = get_user_model()

urlpatterns = router.urls
