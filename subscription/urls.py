from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('plans', PlanViewSet)
router.register('subscriptions', SubscriptionViewSet)
router.register('transactions', TransactionViewSet)
router.register('prices', PriceViewSet)

urlpatterns = router.urls
