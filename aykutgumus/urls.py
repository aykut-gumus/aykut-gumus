from django.conf.urls import url, include
from rest_framework import routers
from api.views import JobViewSet, ContactViewSet, SkillViewSet, SocialViewSet, InterestViewSet

router = routers.DefaultRouter()
router.register(r'jobs', JobViewSet)
router.register(r'profiles', SocialViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'interests', InterestViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
